from flasco.repositories.comentario_repository import ComentarioRepository


class UpdateComentarioUseCase: 
    def __init__(
        self,
        comentario_repository: ComentarioRepository,
    ):
        self.comentario_repository = comentario_repository
        
    async def execute(self, id_comentario: str, new_comentario: str): 

        try:
            await self.comentario_repository.update(
                id_comentario=id_comentario,
                new_comentario=new_comentario
            )

        except Exception as e:
            raise ValueError(
                f"Nao foi possivel modificar o comentario"
            )