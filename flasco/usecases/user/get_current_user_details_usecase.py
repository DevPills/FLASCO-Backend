from flasco.repositories.usuario_repository import UsuarioRepository


class GetCurrentUserDetailsUseCase:
    def __init__(self, user_repository: UsuarioRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: str):
        user_details = await self.user_repository.get_user_by_id(user_id)
        return user_details
