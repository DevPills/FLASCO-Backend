from flasco.database.filestorage import SupabaseStorage
from flasco.repositories.video_repository import VideoRepository


class GetVideoUseCase:
    def __init__(
        self,
        video_repository: VideoRepository,
        supabase_service: SupabaseStorage
    ):
        self.supabase_service = supabase_service
        self.video_repository = video_repository

    async def execute(self, video_id: str):
        video_db_result = await self.video_repository.get_video_by_id(video_id)
        if not video_db_result:
            raise ValueError("Video not found")

        video_supabase_result = await self.supabase_service.get_video_url(
            video_db_result.videoaula_path
        )
        if not video_supabase_result:
            raise ValueError("Video not found in Supabase")

        return video_supabase_result
