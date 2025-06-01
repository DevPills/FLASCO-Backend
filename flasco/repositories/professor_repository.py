import uuid
from sqlalchemy import select
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar


from flasco.models.professor import Professor
from flasco.repositories.base_repository import BaseRepository


T = TypeVar("T")


class UserRepository(BaseRepository): 
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Professor)

    async def get_professor_by_id(self, id: uuid) -> Professor:
        query = select(Professor).where(Professor.id_usuario == id)
        result = await self.db_session.execute(query)
        return result.scalars().first()
    
