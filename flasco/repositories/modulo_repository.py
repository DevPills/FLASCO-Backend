from sqlalchemy.ext.asyncio import AsyncSession

from flasco.application.dtos.modulo_dto import ModuloDTO
from flasco.models.modulo import Modulo
from flasco.repositories.base_repository import T, BaseRepository


class ModuloRepository(BaseRepository): 
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
    
    async def create(self, dto: ModuloDTO) -> Modulo:

        modulo = Modulo(
            nome = dto.nome,
            descricao = dto.descricao,
            id_professor_criador = dto.id_professor_criador
        )

        self.db_session.add(modulo)
        await self.db_session.commit()
        await self.db_session.refresh(modulo)

        return modulo
    
    async def get_all_modulos(): 
        return
