import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, load_only
from flasco.application.dtos.user_dto import UserResponseDTO
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Usuario)

    async def get_user_by_email(self, email: str) -> Usuario:
        query = (
            select(Usuario)
            .options(
                selectinload(Usuario.professor),
                selectinload(Usuario.aluno),
            )
            .where(Usuario.email == email)
        )
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_id(self, id_usuario: uuid.UUID) -> UserResponseDTO:
        query = (
            select(
                Usuario
            ).options(
                load_only(
                    Usuario.id_usuario,
                    Usuario.email,
                    Usuario.nome,
                    Usuario.instituicao,
                    Usuario.tipo,
                ),
                selectinload(Usuario.professor),
                selectinload(Usuario.aluno)
            )
            .where(Usuario.id_usuario == id_usuario)
        )
        result = await self.db_session.execute(query)
        user = result.mappings().first()
        return user

    async def delete_user(self, id_usuario: uuid.UUID) -> bool:
        user = await self.db_session.get(Usuario, id_usuario)
        if not user:
            return False
        await self.db_session.delete(user)
        await self.db_session.commit()
        return True
