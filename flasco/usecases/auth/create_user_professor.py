# flasco/usecases/auth/create_user_professor.py

from fastapi import HTTPException
from flasco.application.dtos.auth_dto import ProfessorDTO
from flasco.application.utils.auth import get_password_hash
from flasco.infra.services.jwt_token_service import create_access_token
from flasco.repositories.professor_repository import UserRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserProfessorUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user: ProfessorDTO) -> None:
        professor_user_registered = await self.user_repository.get_professor_by_id(
            user.id
        )

        if professor_user_registered:
            raise HTTPException(
                status_code=400,
                detail="Usuario ja cadastrado"
            )
        user.password = get_password_hash(user.password)
        try:
            await self.user_repository.create(user)
        except Exception as ex:
            raise HTTPException(
                status_code=400,
                detail=f"Não foi possível criar o usuário: {str(ex)}"
            )
        access_token = create_access_token(data={"sub": str(user.id)})
        return {
            "status": "sucesso",
            "mensagem": "Usuário criado com sucesso",
            "access_token": access_token
        }