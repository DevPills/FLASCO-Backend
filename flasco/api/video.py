from fastapi import APIRouter, Depends, File, Request, UploadFile

from flasco.dependencies import video_upload_usecase
from flasco.usecases.video_upload import VideoUploadUseCase

router = APIRouter(prefix="/v1/video", tags=["video"])


@router.post("/upload")
async def upload_video(
    request: Request,
    video_file: UploadFile = File(...),
    usecase: VideoUploadUseCase = Depends(video_upload_usecase)
):
    await usecase.execute(
        video_file=video_file.file,
        video_name=video_file.filename,
        content_type=video_file.content_type,
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
