from fastapi import HTTPException
from flasco.application.dtos.auth_dto import ProfessorDTO
from flasco.application.utils.auth import get_password_hash
from flasco.infra.services.jwt_token_service import create_access_token
from flasco.repositories.professor_repository import ProfessorRepository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class CreateUserProfessorUseCase: 
    def __init__(self, professor_repository: ProfessorRepository):
        self.professor_repository = professor_repository

    async def execute(self, user: ProfessorDTO) -> None:
        professor_user_registered = await self.professor_repository.get_professor_by_email(
            user.email #podemos pesquisar o professor pelo email
        )
        if professor_user_registered:
            raise HTTPException(
                status_code=400,
                detail="Usuario ja cadastrado"
            )
        user.senha = get_password_hash(user.senha)
        try:
            await self.professor_repository.create(user)
        except Exception as ex: 
            raise HTTPException(
                status_code=400,
                detail=f"Não foi possível criar o usuário: {str(ex)}"
            )
        access_token =  create_access_token(data={})
        return {
            "status": "sucesso",
            "mensagem": "Usuário criado com sucesso",
            "access_token": access_token
        }
()