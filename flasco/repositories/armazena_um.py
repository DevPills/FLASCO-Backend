from sqlalchemy.ext.asyncio import AsyncSession
from flasco.models.armazena_um import ArmazenaUm
from flasco.repositories.base_repository import BaseRepository


class ArmazenaUmRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, ArmazenaUm)
