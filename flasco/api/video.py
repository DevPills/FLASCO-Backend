from fastapi import APIRouter, Depends, File, Request, UploadFile, Query

from flasco.dependencies import (
    video_upload_usecase,
    video_list_usecase
)
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.usecases.video_list import VideoListUseCase

router = APIRouter(prefix="/v1/video", tags=["video"])


@router.post("/upload")
async def upload_video(
    request: Request,
    video_name: str = File(...),
    video_file: UploadFile = File(...),
    usecase: VideoUploadUseCase = Depends(video_upload_usecase)
):
    contents = await video_file.read()
    await usecase.execute(
        video_name=video_name,
        contents=contents,
    )
    return {
        "status": "success",
        "filename": video_file.filename
    }

# @router.delete("/delete")
# async def delete_video(
#     request: Request,
#     title: str,
#     file: DeleteFile
# ):
#     ...
@router.get("/list")
async def list_videos(
    request: Request,
    limit: int | None = Query(None, ge=1, description="Máximo de itens"),
    offset: int = Query(0, ge=0, description="Deslocamento inicial"),
    usecase: VideoListUseCase = Depends(video_list_usecase)
):
    videos = await usecase.execute(limit=limit, offset=offset)
    return {
        "status": "success",
        "items": len(videos),
        "videos": videos
    }