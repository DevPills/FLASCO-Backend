from fastapi import HTTPException
from flasco.application.dtos.modulo_dto import ModuloDTO
from flasco.models.modulo import Modulo
from flasco.repositories.modulo_repository import ModuloRepository


class CreateModuloUseCase:
    def __init__(
        self,
        modulo_respoitory: ModuloRepository
    ):
        self.modulo_repository = modulo_respoitory

    async def execute(self, modulo: ModuloDTO, current_user_id: str) -> None:
        try:
            modulo = await self.modulo_repository.create(modulo)
        except Exception as ex:
            raise HTTPException(
                status_code=400,
                detail=f"Não foi possível criar o modulo: {str(ex)}"
            )
