from flasco.database.filestorage import SupabaseStorage


class DeleteVideoUseCase: 
    def __init__(self, supabase_service: SupabaseStorage):
        self.video_service = supabase_service
    
    async def execute(self, video_name, paths):
        response = await self.video_service.remove(
            file_name=video_name,
            paths=paths
        )
        return response