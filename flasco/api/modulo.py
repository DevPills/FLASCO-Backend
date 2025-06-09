from typing import List
from fastapi import APIRouter, Depends, Request, status

from flasco.application.dtos.modulo_dto import (
    ModuloDTO,
    FavoriteModuloResponseDTO
)
from flasco.infra.middleware.verification_token_middleware import (
    verification_token
)
from flasco.usecases.modulo.create_modulo_usecase import CreateModuloUseCase

from flasco.dependencies import (
    create_modulo_usecase,
    delete_favorite_modulo_usecase,
    favorite_module_usecase,
    get_all_modulos_usecase,
    get_favorited_modulos_usecase,
    swagger_security
)
from flasco.usecases.modulo.delete_modulo_usecase import DeleteModuloUseCase
from flasco.usecases.modulo.favorite_modulo_usecase import FavoriteModuloUseCase
from flasco.usecases.modulo.get_all_modulos_usecase import GetAllModulosUseCase
from flasco.usecases.modulo.get_favorited_modulos_usecase import GetFavoritedModulosUseCase

router = APIRouter(prefix="/modulo", tags=["Modulo"], dependencies=[Depends(swagger_security)])


@router.post("/create", status_code=status.HTTP_201_CREATED)
@verification_token
async def create_modulo(
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


@router.post("/favoritar/{modulo_id}", status_code=status.HTTP_201_CREATED)
@verification_token
async def favoritar_modulo(
    request: Request,
    modulo_id: str,
    usecase: FavoriteModuloUseCase = Depends(favorite_module_usecase)
):
    current_user = request.state.user
    await usecase.execute(
        id_modulo=modulo_id,
        id_usuario=current_user.user_id
    )
    return FavoriteModuloResponseDTO(
        status="Sucesso",
        message="Modulo favoritado com sucesso",
    )


@router.delete(
    "/desfavoritar/{modulo_id}",
    status_code=status.HTTP_200_OK
)
@verification_token
async def delete_favoritar_modulo(
    request: Request,
    modulo_id: str,
    usecase: DeleteModuloUseCase = Depends(delete_favorite_modulo_usecase)
):
    current_user = request.state.user
    await usecase.execute(
        id_modulo=modulo_id,
        id_usuario=current_user.user_id
    )
    return FavoriteModuloResponseDTO(
        status="Sucesso",
        message="Modulo desfavoritado com sucesso",
    )

@router.get("/list", status_code=status.HTTP_200_OK)
@verification_token
async def get_all_modulos(
    request: Request,
    usecase: GetAllModulosUseCase = Depends(get_all_modulos_usecase),
):
    modulos = await usecase.execute()
    return {
        "status": "success",
        "modulos": modulos
    }

@router.get("/favoritos", status_code=status.HTTP_200_OK)
@verification_token
async def get_favorited_modulos(
    request: Request,
    usecase: GetFavoritedModulosUseCase = Depends(get_favorited_modulos_usecase),
):
    current_user = request.state.user
    modulos = await usecase.execute(user_id=current_user.user_id)
    return {
        "status": "success",
        "modulos": modulos
    }
