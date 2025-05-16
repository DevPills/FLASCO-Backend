from flasco.database.filestorage import SupabaseStorage
from flasco.models.video import Video
from flasco.repositories.video_repository import VideoRepository
from uuid import UUID
from datetime import time


class VideoUploadUseCase:
    def __init__(
        self,
        supabase_service: SupabaseStorage,
        video_repository: VideoRepository,
    ):
        self.video_service = supabase_service
        self.video_repository = video_repository

    async def execute(self, video_name, contents):
        filestorage_uploaded = await self.video_service.upload(
            file_name=video_name,
            contents=contents,
        )

        duracao_time = time(0, 0, 0)

        video = Video(
            nome=video_name,
            descricao="blablabla",
            duracao=duracao_time,
            videoaula_path=filestorage_uploaded.full_path,
            id_professor=UUID("70e2e8d8-6909-4761-998f-4b2b417ca4ff"),
        )

        response = await self.video_repository.create(item=video)

        return response
