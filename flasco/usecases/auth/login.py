from fastapi import HTTPException, status

from flasco.application.dtos.auth_dto import LoginDTO
from flasco.application.utils.auth import verify_password
from flasco.infra.services.jwt_token_service import create_access_token
from flasco.repositories.usuario_repository import UsuarioRepository


class LoginUseCase:
    def __init__(self, user_repository: UsuarioRepository):
        self.user_repository = user_repository

    async def execute(self, login_data: LoginDTO):
        print(f"Attempting login for email: {login_data.email}")
        user = await self.user_repository.get_by_email(login_data.email)
        
        if not user:
            print(f"User not found for email: {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha inválidos",
            )

        print(f"User found: {user.email}, verifying password...")
        if not verify_password(login_data.password, user.senha):
            print(f"Invalid password for user: {user.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email ou senha inválidos",
            )

        print(f"Password verified successfully for user: {user.email}")
        access_token = create_access_token(
            {"user_id": str(user.id_usuario), "email": user.email}
        )
        return {"access_token": access_token, "token_type": "bearer"}
