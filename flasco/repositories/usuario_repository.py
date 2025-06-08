from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Usuario)

    async def get_user_by_email(self, email: str) -> Usuario:
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db_session.execute(query)
        return result.scalars().first()
