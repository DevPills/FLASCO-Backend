from http import HTTPStatus
from fastapi import APIRouter, Depends, File, Query, Request, UploadFile

from flasco.application.dtos.auth_dto import ProfessorDTO
from flasco.dependencies import create_professor_user_usecase
from flasco.usecases.auth.create_user_professor import CreateUserProfessorUseCase

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/professor")
async def create_usuario_professor(
    request: Request,
    professor_data: ProfessorDTO,
    create_user_usecase: CreateUserProfessorUseCase = Depends(create_professor_user_usecase)
): 
    response = await create_user_usecase.execute(professor_data)
    return response