import enum
from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base
from flasco.models.usuario import Usuario
from flasco.models.se_matricula import SeMatricula


class CursoEnum(enum.Enum):
    TECNICO_DE_INFORMATICA = "TECNICO_DE_INFORMATICA"
    ENGENHARIA_DE_SOFTWARE = "ENGENHARIA_DE_SOFTWARE"
    ENGENHARIA_DE_COMPUTACAO = "ENGENHARIA_DE_COMPUTACAO"
    SISTEMAS_DE_INFORMACAO = "SISTEMAS_DE_INFORMACAO"
    ANALISE_DESENVOLVIMENTO_DE_SISTEMAS = (
        "ANALISE_DESENVOLVIMENTO_DE_SISTEMAS"
    )
    ENGENHARIA_DE_INFORMACAO = "ENGENHARIA_DE_INFORMACAO"
    CIENCIA_DA_COMPUTACAO = "CIENCIA_DA_COMPUTACAO"


class Aluno(Base):
    __tablename__ = "aluno"

    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True
    )

    curso: Mapped[CursoEnum | None] = mapped_column(
        Enum(CursoEnum, name="curso_enum", native_enum=True),
        nullable=True
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="aluno",
    )

    modulos_matriculados: Mapped[list["SeMatricula"]] = relationship(
        back_populates="aluno",
        cascade="all, delete-orphan",
    )