from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar


T = TypeVar("T")


class VideoRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, item: T) -> T:
        self.db_session.add(item)
        await self.db_session.commit()
        await self.db_session.refresh(item)

        return item
    
    async def delete(self, item: T) -> T:
        self.db_session.delete(item)
        await self.db_session.commit()
        await self.db_session.refresh(item)
