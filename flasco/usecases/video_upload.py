from flasco.application.dtos.modulo_dto import ArmazenaUmDTO
from flasco.database.filestorage import SupabaseStorage
from flasco.models.video import Video
from flasco.repositories.armazena_um import ArmazenaUmRepository
from flasco.repositories.video_repository import VideoRepository
from uuid import UUID
from datetime import time


class VideoUploadUseCase:
    def __init__(
        self,
        supabase_service: SupabaseStorage,
        video_repository: VideoRepository,
        armazena_um_repository: ArmazenaUmRepository,
    ):
        self.video_service = supabase_service
        self.video_repository = video_repository
        self.armazena_um_repository = armazena_um_repository

    async def execute(self, video_name, contents, modulo_id=None):
        filestorage_uploaded = await self.video_service.upload(
            file_name=video_name,
            contents=contents,
        )

        duracao_time = time(0, 0, 0)

        video = Video(
            nome=video_name,
            descricao="blablabla",
            duracao=duracao_time,
            videoaula_path=filestorage_uploaded.path,
            id_professor=UUID("fb53ac66-7f07-46e7-81a7-b6901b0de3b3"),
        )

        response = await self.video_repository.create(item=video)

        armazena_um = ArmazenaUmDTO(
            id_video=response.id_video,
            id_modulo=modulo_id,
            posicao=0,
        )

        await self.armazena_um_repository.create(item=armazena_um)

        return response
