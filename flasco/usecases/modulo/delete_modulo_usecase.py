from flasco.repositories.favorito_repository import FavoritoRepository


class DeleteModuloUseCase:
    def __init__(
        self,
        favorito_repository: FavoritoRepository,
    ):
        self.favorito_repository = favorito_repository

    async def execute(self, id_modulo: str, id_usuario: str):

        try:
            await self.favorito_repository.delete_favorite_modulo(
                id_modulo=id_modulo,
                id_usuario=id_usuario
            )
        except Exception as e:
            raise ValueError(
                f"Não foi possível deletar o modulo favorito: {str(e)}"
            )
