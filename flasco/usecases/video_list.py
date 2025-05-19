from flasco.database.filestorage import SupabaseStorage
from flasco.repositories.video_repository import VideoRepository


class VideoListUseCase:
    def __init__(
        self,
        supabase_service: SupabaseStorage,
        video_repository: VideoRepository,
    ):
        self.video_service = supabase_service
        self.video_repository = video_repository

    async def execute(self, limit: int | None = None, offset: int = 0):

        videos = await self.video_repository.get_all_videos()

        return videos
