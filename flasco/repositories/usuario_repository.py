from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from flasco.models.usuario import Usuario


class UsuarioRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_by_email(self, email: str) -> Usuario | None:
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db_session.execute(query)
        return result.scalars().first()
