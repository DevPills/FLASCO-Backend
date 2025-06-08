from fastapi import APIRouter, Depends, Request

from flasco.application.dtos.modulo_dto import ModuloDTO
from flasco.usecases.modulo.create_modulo_usecase import CreateModuloUseCase

from flasco.dependencies import (
    create_modulo_usecase
)

router = APIRouter(prefix="/modulo", tags=["Modulo"])

@router.post("/create")
async def create_video(
    request: Request,
    modulo_data: ModuloDTO,
    create_modulo_usecase: CreateModuloUseCase = Depends(create_modulo_usecase)
): 
    response = await create_modulo_usecase.execute(modulo_data)
    return response
    