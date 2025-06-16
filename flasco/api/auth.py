from uuid import UUID
from fastapi import APIRouter, Depends, Request, status

from flasco.application.dtos.auth_dto import AlunoDTO, LoginDTO, ProfessorDTO
from flasco.dependencies import (
    create_aluno_user_usecase,
    create_professor_user_usecase,
    delete_user_usecase,
    login_usecase
)
from flasco.usecases.auth.create_user_aluno import CreateUserAlunoUseCase
from flasco.usecases.auth.create_user_professor import (
    CreateUserProfessorUseCase
)
from flasco.usecases.auth.delete_user import DeleteUserUseCase
from flasco.usecases.auth.login import LoginUseCase

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/professor")
async def create_usuario_professor(
    request: Request,
    professor_data: ProfessorDTO,
    create_user_usecase: CreateUserProfessorUseCase = Depends(
        create_professor_user_usecase
    )
):
    response = await create_user_usecase.execute(professor_data)
    return response


@router.post("/aluno")
async def create_usuario_aluno(
    request: Request,
    professor_data: AlunoDTO,
    create_user_usecase: CreateUserAlunoUseCase = Depends(
        create_aluno_user_usecase
    )
):
    response = await create_user_usecase.execute(professor_data)
    return response


@router.post('/login', status_code=status.HTTP_200_OK)
async def login(
    request: Request,
    user_data: LoginDTO,
    login_usecase: LoginUseCase = Depends(login_usecase)
):
    response = await login_usecase.execute(user_data)
    return response

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(
    user_id: UUID,
    delete_usecase: DeleteUserUseCase = Depends(delete_user_usecase),
):
    return await delete_usecase.execute(user_id)