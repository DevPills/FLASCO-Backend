from flasco.application.dtos.comentario_dto import UpdateComentarioDTO
from flasco.repositories.comentario_repository import ComentarioRepository
from fastapi import HTTPException


class UpdateComentarioUseCase:
    def __init__(
        self,
        comentario_repository: ComentarioRepository,
    ):
        self.comentario_repository = comentario_repository

    async def execute(
        self,
        id_comentario: str,
        new_comentario: UpdateComentarioDTO
    ):
        try:
            await self.comentario_repository.update_comentario(
                comentario_id=id_comentario,
                new_comentario=new_comentario.novo_comentario
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Nao foi possivel modificar o comentario: {e}"
            )
