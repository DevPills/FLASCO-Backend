from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Usuario)

    async def get_user_by_email(self, email: str) -> Usuario | None:
        print(f"Searching for user with email: {email}")
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db_session.execute(query)
        user = result.scalars().first()
        if user:
            print(f"Found user: {user.email}, hash: {user.senha[:20]}...")
        else:
            print("No user found")
        return user
