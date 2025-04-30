from flasco.database.filestorage import SupabaseStorage


class VideoUploadUseCase:
    def __init__(self, supabase_service: SupabaseStorage):
        self.video_service = supabase_service

    async def execute(self, video_file, video_name, content_type):
        response = await self.video_service.upload(
            file=video_file,
            file_name="video_name",
            content_type=content_type,
        )

        return response
