from flasco.models.favorita_um import FavoritaUm
from flasco.repositories.base_repository import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

class FavoritoRepository(BaseRepository):
    def __init__(self,db_session: AsyncSession):
        super().__init__(db_session, FavoritaUm)
    
        