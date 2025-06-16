from uuid import UUID
from fastapi import HTTPException, status
from flasco.repositories.usuario_repository import UsuarioRepository


class DeleteUserUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    async def execute(self, user_id: UUID) -> dict:
        success = await self.usuario_repository.delete_user(user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Falha ao deletar o usuário"
            )
        return {
            "status": "sucesso",
            "mensagem": "Usuário deletado com sucesso",
            "codigo": status.HTTP_200_OK,
        }
