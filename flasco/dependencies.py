from fastapi import Depends
from flasco.database.filestorage import SupabaseStorage
from flasco.database.database import get_async_session
from flasco.repositories.video_repository import VideoRepository
from flasco.usecases.video_upload import VideoUploadUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from flasco.settings import settings


def get_supabase_service() -> SupabaseStorage:
    return SupabaseStorage(
        bucket=settings.SUPABASE_BUCKET,
    )


def get_video_repository(
    session: AsyncSession = Depends(get_async_session),
):
    return VideoRepository(db_session=session)


def video_upload_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository
    )
