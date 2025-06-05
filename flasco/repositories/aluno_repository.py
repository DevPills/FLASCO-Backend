

from typing import Optional
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import String, inspect, select
from flasco.application.dtos.auth_dto import AlunoDTO
from flasco.application.enums.curso import Curso
from flasco.models.aluno import Aluno, CursoEnum
from flasco.models.professor import FormacaoEnum
from flasco.models.usuario import Usuario
from flasco.repositories.base_repository import BaseRepository


class AlunoRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session, Aluno)
    
    async def get_aluno_by_email(self, email: str) -> Usuario:
        query = select(Usuario).where(Usuario.email == email)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def get_user_by_id(self, id_usuario: uuid.UUID) -> Optional[Usuario]:
        query = select(Usuario).where(Usuario.id_usuario == id_usuario)
        result = await self.db_session.execute(query)
        return result.scalars().first()

    async def upsert_user(self, dto: AlunoDTO) -> Usuario:

        data = dto.model_dump()


        usuario = Usuario(
            nome=dto.nome,
            email=dto.email,
            instituicao=dto.instituicao,
            senha=dto.password
        )

        self.db_session.add(usuario)
        await self.db_session.flush()
        return usuario

    async def create(self, dto: AlunoDTO) -> Aluno:
        usuario = await self.upsert_user(dto)

        curso_enum = (
            CursoEnum[dto.curso.name.upper()]
            if hasattr(dto.curso, "name")
            else CursoEnum[dto.curso.upper()]
            if dto.curso
            else None
        )

        aluno = Aluno(
            id_usuario=usuario.id_usuario,
            curso=curso_enum,
        )
        self.db_session.add(aluno)

        await self.db_session.commit()
        await self.db_session.refresh(aluno)
        return aluno