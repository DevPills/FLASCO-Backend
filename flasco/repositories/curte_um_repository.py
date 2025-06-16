from sqlalchemy import delete
from flasco.models.curte_um import CurteUm
from flasco.repositories.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class CurteUmRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, CurteUm)

    async def delete_curte_um_video(self, id_video: str, id_usuario):
        stmt = delete(CurteUm).where(
            (CurteUm.id_video == id_video) &
            (CurteUm.id_usuario == id_usuario)
        )

        await self.db_session.execute(stmt)
        await self.db_session.commit()
