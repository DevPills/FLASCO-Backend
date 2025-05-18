from http import HTTPStatus
import uuid
from fastapi import APIRouter, Depends, File, Request, UploadFile

from flasco.dependencies import video_delete_usecase, video_upload_usecase
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_upload import VideoUploadUseCase

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
