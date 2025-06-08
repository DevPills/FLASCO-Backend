import uuid
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from flasco.models.professor import Professor, FormacaoEnum
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository
from flasco.application.dtos.auth_dto import ProfessorDTO


class ProfessorRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Professor)

    async def get_professor_by_email(self, email: str) -> Usuario:
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_id(self, id_usuario: uuid.UUID) -> Optional[Usuario]:
        query = select(Usuario).where(Usuario.id_usuario == id_usuario)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def upsert_user(self, dto: ProfessorDTO) -> Usuario:
        usuario = Usuario(
            nome=dto.nome,
            email=dto.email,
            instituicao=dto.instituicao,
            senha=dto.password
        )

        self.db_session.add(usuario)
        await self.db_session.flush()
        return usuario

    async def create(self, dto: ProfessorDTO) -> Professor:
        usuario = await self.upsert_user(dto)

        formacao_enum = (
            FormacaoEnum[dto.formacao.name.upper()]
            if hasattr(dto.formacao, "name")
            else FormacaoEnum[dto.formacao.upper()]
            if dto.formacao
            else None
        )

        professor = Professor(
            id_usuario=usuario.id_usuario,
            formacao=formacao_enum,
        )
        self.db_session.add(professor)

        await self.db_session.commit()
        await self.db_session.refresh(professor)
        return professor
