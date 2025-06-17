from flasco.repositories.comentario_repository import ComentarioRepository


class DeleteComentarioUseCase:
    def __init__(
        self,
        comentario_repository: ComentarioRepository,
    ):
        self.comentario_repository = comentario_repository

    async def execute(self, id_comentario: str, id_usuario: str):

        try:
            await self.comentario_repository.delete_comentario(
                id_comentario=id_comentario,
                id_usuario=id_usuario
            )
        except Exception as e:
            raise ValueError(
                f"Não foi possível deletar o comentário"
            )