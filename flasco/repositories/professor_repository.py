import uuid
from sqlalchemy import select
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from typing import TypeVar


from flasco.models.professor import Professor
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


T = TypeVar("T")


class ProfessorRepository(BaseRepository): 
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Professor)

    async def get_professor_by_email(self, email: str) -> Professor | None:
        query = (
            select(Professor)
            .join(Professor.usuario)
            .options(joinedload(Professor.usuario))
            .where(Usuario.email == email)
        )#deveriamos pesquisar se existe um usuario qlqr ou podemos ter 2 cadastros separados?
        result = await self.db_session.execute(query)
        return result.scalars().first()
    
