from flasco.database.filestorage import SupabaseStorage
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.settings import settings
from flasco.usecases.video_list import VideoListUseCase


def get_supabase_service() -> SupabaseStorage:
    return SupabaseStorage(
        bucket=settings.SUPABASE_BUCKET,
    )


def video_upload_usecase() -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=get_supabase_service()
    )

def video_list_usecase() -> VideoListUseCase:
    return VideoListUseCase(
        supabase_service=get_supabase_service()
    )