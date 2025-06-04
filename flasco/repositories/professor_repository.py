import uuid
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.inspection import inspect

from flasco.models.professor import Professor, FormacaoEnum
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository
from flasco.application.dtos.auth_dto import ProfessorDTO


class UserRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Professor)

    async def get_professor_by_id(self, id: uuid) -> Professor:
        query = select(Professor).where(Professor.id_usuario == id)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_id(self, id_usuario: uuid.UUID) -> Optional[Usuario]:
        query = select(Usuario).where(Usuario.id_usuario == id_usuario)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def upsert_user(self, dto: ProfessorDTO) -> Usuario:
        usuario = await self.get_user_by_id(dto.id)
        if usuario:
            return usuario

        data = dto.model_dump()

        cols = {c.key for c in inspect(Usuario).mapper.column_attrs}
        usuario_data = {k: v for k, v in data.items() if k in cols}

        if "password" in data and "senha" in cols:
            usuario_data["senha"] = data["password"]
        elif "password" in data:
            usuario_data["password"] = data["password"]

        usuario_data["id_usuario"] = dto.id

        usuario = Usuario(**usuario_data)
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