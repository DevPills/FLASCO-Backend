from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy import delete, select
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar

from flasco.models.video import Video


T = TypeVar("T")


class VideoRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, item: T) -> T:
        self.db_session.add(item)
        await self.db_session.commit()
        await self.db_session.refresh(item)

        return item
    
    async def delete_video_by_id(self, video_id: str):

        query = delete(Video).where(Video.id_video == video_id)
        result = await self.db_session.execute(query)
        await self.db_session.commit()
        

        deleted_video = result
        if not result:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Video nao existe"
            )
        
        
        return deleted_video
    
    async def get_video_by_id(self, video_id: str) -> T:
        query = select(Video).where(Video.id_video == video_id)
        result = await self.db_session.execute(query)
        video = result.scalars().first()
        if not video:
            return None
        return video
