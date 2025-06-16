from flasco.application.dtos.video_dto import LikeVideoDTO
from flasco.repositories.curte_um_repository import CurteUmRepository


class LikeVideoUseCase:
    def __init__(self, curte_um_repository: CurteUmRepository,):
        self.curte_um_repository = curte_um_repository

    async def execute(self, id_video: str, id_usuario: str):
        modulo_favoritado = LikeVideoDTO(
            id_video=id_video,
            id_usuario=id_usuario
        )

        return await self.curte_um_repository.create(
            item=modulo_favoritado
        )
