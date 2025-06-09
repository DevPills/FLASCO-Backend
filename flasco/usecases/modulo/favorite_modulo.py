from flasco.application.dtos.modulo_dto import FavoriteModuloDTO
from flasco.repositories.favorito_repository import FavoritoRepository


class FavoriteModuloUseCase:
    def __init__(
        self,
        favorito_repository: FavoritoRepository,
    ):
        self.favorito_repository = favorito_repository

    async def execute(self, id_modulo: str, id_usuario: str):
        modulo_favoritado = FavoriteModuloDTO(
            id_modulo=id_modulo,
            id_usuario=id_usuario
        )

        return await self.favorito_repository.create(
            item=modulo_favoritado
        )
