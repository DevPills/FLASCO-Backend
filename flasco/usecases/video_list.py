from flasco.database.filestorage import SupabaseStorage


class VideoListUseCase:
    def __init__(self, supabase_service: SupabaseStorage):
        self.video_service = supabase_service

    async def execute(self, limit: int | None = None, offset: int = 0):
        return await self.video_service.list_files(
            limit=limit,
            offset=offset,
        )
