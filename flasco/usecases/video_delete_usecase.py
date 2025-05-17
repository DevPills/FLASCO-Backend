from datetime import time
from flasco.database.filestorage import SupabaseStorage
from flasco.repositories.video_repository import VideoRepository


class DeleteVideoUseCase: 
    def __init__(self, supabase_service: SupabaseStorage, video_respository: VideoRepository):
        self.video_service = supabase_service
        self.video_respository = video_respository
    
    async def execute(self, video_name, paths):
        deleted_video = await self.video_service.remove(
            file_name=video_name,
            paths=paths
        )
        
        response = await self.video_respository.delete(item=deleted_video)

        return response