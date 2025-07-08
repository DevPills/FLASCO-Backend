from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, or_, update
from sqlalchemy.orm import selectinload 
from flasco.models.comentario import Comentario
from flasco.models.video import Video
from flasco.application.dtos.comentario_dto import ComentarioDTO
from typing import List, Optional
from flasco.repositories.base_repository import T, BaseRepository

class ComentarioRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Comentario)


    async def create(self, data: ComentarioDTO) -> Comentario:
        comentario = Comentario(**data.model_dump())
        self.db_session.add(comentario)
        await self.db_session.commit()
        await self.db_session.refresh(comentario)
        return comentario
    

    async def delete_comentario(self, id_comentario: str, id_usuario: str):
        stmt = delete(Comentario).where(
            (Comentario.id_comentario == id_comentario),
            or_(Comentario.id_usuario == id_usuario,
                Comentario.video.has(Video.id_professor == id_usuario)
                )
        )

        await self.db_session.execute(stmt)
        await self.db_session.commit()


    async def get_by_id(self, comentario_id: str) -> Optional[Comentario]:
        stmt = select(Comentario).where(Comentario.id_comentario == comentario_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()
    

    async def get_comentarios_by_video_id(self, video_id: str) -> List[Comentario]:
        stmt = (
            select(Comentario)
            .where(Comentario.id_video == video_id)
            .options(selectinload(Comentario.usuario))  # <- carrega o usuário relacionado
        )
        result = await self.db_session.execute(stmt)
        return result.scalars().all()
    

    async def update_comentario(self, comentario_id: str, new_comentario: str): 

        stmt = (
            update(self.model)
            .where(self.model.comentario_id == int(comentario_id))
            .values(**new_comentario)
        )
        await self.db_session.execute(stmt)
        await self.db_session.commit()

        result = await self.get_by_id(comentario_id)
        return result


