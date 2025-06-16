from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from flasco.models.comentario import Comentario
from flasco.application.dtos.comentario_dto import ComentarioDTO
from typing import List, Optional
from flasco.repositories.base_repository import BaseRepository

class ComentarioRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Comentario)

    async def create(self, data: ComentarioDTO) -> Comentario:
        comentario = Comentario(**data.model_dump())
        self.db_session.add(comentario)
        await self.db_session.commit()
        await self.db_session.refresh(comentario)
        return comentario
    
    async def get_by_id(self, comentario_id: str) -> Optional[Comentario]:
        stmt = select(Comentario).where(Comentario.id_comentario == comentario_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()


    async def get_comentarios_by_video_id(self, video_id: str) -> List[Comentario]:
        stmt = select(Comentario).where(Comentario.id_video == video_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().all()
    
