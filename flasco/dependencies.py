from flasco.database.filestorage import SupabaseStorage
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.settings import settings


def get_supabase_service() -> SupabaseStorage:
    return SupabaseStorage(
        bucket=settings.SUPABASE_BUCKET,
    )


def video_upload_usecase() -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=get_supabase_service()
    )


def video_delete_usecase() -> DeleteVideoUseCase:
    return DeleteVideoUseCase(
        supabase_service=get_supabase_service()
    )
