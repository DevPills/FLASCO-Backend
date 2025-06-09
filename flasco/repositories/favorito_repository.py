from sqlalchemy import select
import uuid
from sqlalchemy import delete
from flasco.models.favorita_um import FavoritaUm
from flasco.repositories.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession


class FavoritoRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, FavoritaUm)

    async def delete_favorite_modulo(self, id_modulo: str, id_usuario):
        stmt = delete(FavoritaUm).where(
            (FavoritaUm.id_modulo == id_modulo) &
            (FavoritaUm.id_usuario == id_usuario)
        )

        await self.db_session.execute(stmt)
        await self.db_session.commit()
        
    async def get_favorited_module_ids_by_user(
        self, user_id: uuid.UUID
    ) -> list[uuid.UUID]:
        stmt = select(self.model.id_modulo).where(self.model.id_usuario == user_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().all()
