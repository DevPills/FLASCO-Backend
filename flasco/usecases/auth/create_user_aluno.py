from fastapi import HTTPException
from flasco.application.dtos.auth_dto import AlunoDTO
from flasco.application.utils.auth import get_password_hash
from flasco.infra.services.jwt_token_service import create_access_token
from flasco.repositories.aluno_repository import AlunoRepository


class CreateUserAlunoUseCase: 
    def __init__(self, aluno_repository: AlunoRepository):
        self.aluno_repository = aluno_repository

    async def execute(self, user: AlunoDTO) -> None:
        aluno_user_registered = await self.aluno_repository.get_aluno_by_id(
            user.id
        )

        if aluno_user_registered:
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