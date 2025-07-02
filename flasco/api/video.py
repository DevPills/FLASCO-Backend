from http import HTTPStatus
from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Query,
    Request,
    UploadFile,
    status
)
from fastapi.responses import StreamingResponse

from flasco.dependencies import (
    dislike_video_usecase,
    get_video_usecase,
    like_video_usecase,
    list_video_usecase,
    video_delete_usecase,
    video_upload_usecase
)
from flasco.infra.middleware.verification_token_middleware import (
    verification_token
)
from flasco.usecases.dislike_video import DislikeVideoUseCase
from flasco.usecases.like_video import LikeVideoUseCase
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_get import GetVideoUseCase
from flasco.usecases.video_list import VideoListUseCase
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.gateways.video_stream import VideoStreamGateway

router = APIRouter(prefix="/v1/video", tags=["video"])


@router.post("/upload")
async def upload_video(
    request: Request,
    video_name: str = File(...),
    video_file: UploadFile = File(...),
    modulo_id: str = Form(...),
    usecase: VideoUploadUseCase = Depends(video_upload_usecase)
):
    contents = await video_file.read()
    response = await usecase.execute(
        video_name=video_name,
        contents=contents,
        modulo_id=modulo_id
    )
    return response


@router.delete("/delete/{video_id}", status_code=HTTPStatus.OK)
async def delete_video(
    request: Request,
    video_id: str,
    file_name: str = File(...),
    paths: str = File(...),
    usecase: DeleteVideoUseCase = Depends(video_delete_usecase),
):
    await usecase.execute(
        video_name=file_name,
        paths=paths,
        video_id=video_id
    )
    return {
        "status": "success",
        "deletedvideo": file_name,
        "paths": paths
    }


@router.get("/get-video/{video_id}", status_code=HTTPStatus.OK)
async def get_video_url(
    request: Request,
    video_id: str,
    get_video_usecase: GetVideoUseCase = Depends(get_video_usecase)
):
    response = await get_video_usecase.execute(
        video_id=video_id
    )
    return StreamingResponse(
        VideoStreamGateway.start_stream(video_url=response),
        media_type="video/mp4"
    )


@router.get("/list")
async def list_videos(
    request: Request,
    limit: int | None = Query(None, ge=1, description="Máximo de itens"),
    offset: int = Query(0, ge=0, description="Deslocamento inicial"),
    usecase: VideoListUseCase = Depends(list_video_usecase)
):
    videos = await usecase.execute(limit=limit, offset=offset)
    return {
        "status": "success",
        "items": len(videos),
        "videos": videos
    }


@router.post("/like/{video_id}", status_code=status.HTTP_201_CREATED)
@verification_token
async def like_video(
    request: Request,
    video_id: str,
    usecase: LikeVideoUseCase = Depends(like_video_usecase)
):
    current_user = request.state.user
    await usecase.execute(
        id_video=video_id,
        id_usuario=current_user.user_id
    )
    return {
        "status": "success",
        "message": f"Video {video_id} liked by user {current_user.user_id}",
    }


@router.delete("/dislike/{video_id}", status_code=status.HTTP_200_OK)
@verification_token
async def dislike_video(
    request: Request,
    video_id: str,
    usecase: DislikeVideoUseCase = Depends(dislike_video_usecase)
):
    current_user = request.state.user
    await usecase.execute(
        id_video=video_id,
        id_usuario=current_user.user_id
    )
    return {
        "status": "success",
        "message": f"Video {video_id} disliked by user {current_user.user_id}",
    }
