from typing import TypeVar

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class BaseRepository:
    def __init__(self, db_session: AsyncSession, model: T):
        self.db_session = db_session
        self.model = model

    async def create(self, item: T) -> T:
        db_item_data = self.model(**item.model_dump())
        self.db_session.add(db_item_data)
        await self.db_session.commit()
        await self.de_session.refresh(db_item_data)

        return db_item_data

    async def list(self) -> T:
        stmt = select(self.model)
        return await self.db_session.execute(stmt)

    async def get_by_id(self, item_id: str) -> T:
        stmt = select(self.model).where(self.model.id == int(item_id))
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def update(self, item_id: str, update_item_data: T) -> T:
        stmt = (
            update(self.model)
            .where(self.model.id == int(item_id))
            .values(**update_item_data.model_dump())
        )
        await self.db_session.execute(stmt)
        await self.db_session.commit()

        result = await self.get_by_id(item_id)
        return result

    async def delete(self, item_id: str):
        stmt = delete(self.model).where(self.model.id == int(item_id))

        await self.db_session.execute(stmt)
        await self.db_session.commit()
