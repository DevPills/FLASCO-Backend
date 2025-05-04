from flasco.database.filestorage import SupabaseStorage


class VideoUploadUseCase:
    def __init__(self, supabase_service: SupabaseStorage):
        self.video_service = supabase_service

    async def execute(self, video_name, contents):
        response = await self.video_service.upload(
            file_name=video_name,
            contents=contents,
        )

        return response
