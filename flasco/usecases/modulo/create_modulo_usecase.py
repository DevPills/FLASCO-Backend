from fastapi import HTTPException
from flasco.application.dtos.modulo_dto import CreateModuloDTO
from flasco.repositories.modulo_repository import ModuloRepository

class CreateModuloUseCase:
    def __init__(self, modulo_repository: ModuloRepository):
        self.modulo_repository = modulo_repository

    async def execute(self, modulo: CreateModuloDTO):
        try:
            modulo_criado = await self.modulo_repository.create(modulo)

            return {
                "id_modulo": modulo_criado.id_modulo,
                "nome": modulo_criado.nome,
                "descricao": modulo_criado.descricao,
            }

        except Exception as ex:
            raise HTTPException(
                status_code=400,
                detail=f"Não foi possível criar o modulo: {str(ex)}"
            )
