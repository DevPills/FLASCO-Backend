from flasco.repositories.curte_um_repository import CurteUmRepository


class DislikeVideoUseCase:
    def __init__(self, curte_um_repository: CurteUmRepository,):
        self.curte_um_repository = curte_um_repository

    async def execute(self, id_video: str, id_usuario: str):

        try:
            await self.curte_um_repository.delete_curte_um_video(
                id_video=id_video,
                id_usuario=id_usuario
            )
        except Exception as e:
            raise ValueError(
                f"Não foi possível descurtir o video: {str(e)}"
            )
