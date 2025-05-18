from http import HTTPStatus
import uuid
from fastapi import APIRouter, Depends, File, Request, UploadFile
from fastapi.responses import StreamingResponse

from flasco.dependencies import (
    get_video_usecase,
    video_delete_usecase,
    video_upload_usecase
)
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_get import GetVideoUseCase
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.gateways.video_stream import VideoStreamGateway

router = APIRouter(prefix="/v1/video", tags=["video"])


@router.post("/upload")
async def upload_video(
    request: Request,
    video_name: str = File(...),
    video_file: UploadFile = File(...),
    usecase: VideoUploadUseCase = Depends(video_upload_usecase)
):
    contents = await video_file.read()
    response = await usecase.execute(
        video_name=video_name,
        contents=contents,
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
