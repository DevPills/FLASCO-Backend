

from typing import Optional
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import inspect, select
from flasco.application.dtos.auth_dto import AlunoDTO
from flasco.models.aluno import Aluno
from flasco.models.professor import FormacaoEnum
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


class AlunoRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Aluno)

    async def get_aluno_by_id(self, id: uuid) -> Aluno:
        query = select(Aluno).where(Aluno.id_usuario == id)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_id(self, id_usuario: uuid.UUID) -> Optional[Usuario]:
        query = select(Usuario).where(Usuario.id_usuario == id_usuario)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def upsert_user(self, dto: AlunoDTO) -> Usuario:
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

    async def create(self, dto: AlunoDTO) -> Aluno:
        usuario = await self.upsert_user(dto)

        curso_enum = (
            FormacaoEnum[dto.curso.name.upper()]
            if hasattr(dto.curso, "name")
            else FormacaoEnum[dto.curso.upper()]
            if dto.curso
            else None
        )

        aluno = Aluno(
            id_usuario=usuario.id_usuario,
            formacao=FormacaoEnum,
        )
        self.db_session.add(aluno)

        await self.db_session.commit()
        await self.db_session.refresh(aluno)
        return aluno