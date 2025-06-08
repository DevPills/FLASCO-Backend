from fastapi import APIRouter, Depends, Request

from flasco.application.dtos.modulo_dto import ModuloDTO
from flasco.infra.middleware.verification_token_middleware import (
    verification_token
)
from flasco.usecases.modulo.create_modulo_usecase import CreateModuloUseCase

from flasco.dependencies import (
    create_modulo_usecase
)

router = APIRouter(prefix="/modulo", tags=["Modulo"])


@router.post("/create")
@verification_token
async def create_video(
    request: Request,
    modulo_data: ModuloDTO,
    create_modulo_usecase: CreateModuloUseCase = Depends(create_modulo_usecase)
):
    current_user = request.state.user
    response = await create_modulo_usecase.execute(
        modulo_data,
        current_user_id=current_user.user_id
    )
    return response
