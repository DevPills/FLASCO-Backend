from flasco.repositories.modulo_repository import ModuloRepository
from flasco.application.dtos.modulo_dto import GetModuloDTO


class GetAllModulosUseCase:
    def __init__(self, modulo_repository: ModuloRepository):
        self.modulo_repository = modulo_repository

    async def execute(self) -> list[GetModuloDTO]:
        modulos = await self.modulo_repository.get_all()
        return [
            GetModuloDTO(
                id_modulo=modulo.id_modulo,
                nome=modulo.nome,
                descricao=modulo.descricao,
            )
            for modulo in modulos
        ]
