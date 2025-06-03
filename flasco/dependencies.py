from fastapi import Depends
from flasco.database.filestorage import SupabaseStorage
from flasco.database.database import get_async_session
from flasco.repositories.professor_repository import ProfessorRepository
from flasco.repositories.video_repository import VideoRepository
from flasco.usecases.auth.create_user_professor import CreateUserProfessorUseCase
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_get import GetVideoUseCase
from flasco.usecases.video_list import VideoListUseCase
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

def professor_repository(
    session: AsyncSession = Depends(get_async_session),
):
    return  ProfessorRepository(db_session=session)

def create_professor_user_usecase(
    professor_repository: ProfessorRepository = Depends(professor_repository),
) -> CreateUserProfessorUseCase:
    return CreateUserProfessorUseCase(professor_repository=professor_repository)


def video_upload_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository
    )


def video_delete_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> DeleteVideoUseCase:
    return DeleteVideoUseCase(
        supabase_service=supabase_service,
        video_respository=video_repository
    )


def get_video_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> GetVideoUseCase:
    return GetVideoUseCase(
        video_repository=video_repository,
        supabase_service=supabase_service
    )


def list_video_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> VideoListUseCase:
    return VideoListUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository
    )
