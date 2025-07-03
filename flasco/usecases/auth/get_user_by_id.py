from uuid import UUID
from flasco.repositories.usuario_repository import UsuarioRepository
from flasco.models.usuario import Usuario


class GetUserByIdUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def execute(self, user_id: UUID) -> Usuario | None:
        return await self.repository.get_user_by_id(user_id)
