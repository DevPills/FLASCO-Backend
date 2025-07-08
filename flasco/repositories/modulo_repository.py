import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from flasco.application.dtos.modulo_dto import ModuloDTO
from flasco.models.modulo import Modulo
from flasco.repositories.base_repository import BaseRepository


class ModuloRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.model = Modulo

    async def create(self, dto: ModuloDTO) -> Modulo:
        modulo = Modulo(
            nome=dto.nome,
            descricao=dto.descricao,
            id_professor_criador=dto.id_professor_criador
        )

        self.db_session.add(modulo)
        await self.db_session.commit()
        await self.db_session.refresh(modulo)

        return modulo

    async def get_all(self) -> list[Modulo]:
        stmt = select(self.model)
        result = await self.db_session.execute(stmt)
        return result.scalars().all()

    async def get_by_ids(self, modulo_ids: list[uuid.UUID]) -> list[Modulo]:
        if not modulo_ids:
            return []
        stmt = select(self.model).where(self.model.id_modulo.in_(modulo_ids))
        result = await self.db_session.execute(stmt)
        return result.scalars().all()
