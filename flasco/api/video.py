from fastapi import APIRouter, Depends, File, Request, UploadFile

from flasco.dependencies import video_upload_usecase
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
