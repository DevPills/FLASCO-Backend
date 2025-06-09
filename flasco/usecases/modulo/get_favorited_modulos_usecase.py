import uuid
from flasco.application.dtos.modulo_dto import GetModuloDTO
from flasco.repositories.modulo_repository import ModuloRepository
from flasco.repositories.favorito_repository import FavoritoRepository


class GetFavoritedModulosUseCase:
    def __init__(
        self,
        modulo_repository: ModuloRepository,
        favorito_repository: FavoritoRepository,
    ):
        self.modulo_repository = modulo_repository
        self.favorito_repository = favorito_repository

    async def execute(self, user_id: uuid.UUID):
        favorited_ids = await self.favorito_repository.get_favorited_module_ids_by_user(
            user_id
        )

        if not favorited_ids:
            return []

        modulos = await self.modulo_repository.get_by_ids(favorited_ids)
        return [
            GetModuloDTO(
                id_modulo=modulo.id_modulo,
                nome=modulo.nome,
                descricao=modulo.descricao,
            )
            for modulo in modulos
        ] 