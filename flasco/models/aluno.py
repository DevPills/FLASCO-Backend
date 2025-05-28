import enum
from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.usuario import Usuario

class CursoEnum(enum.Enum):
    TECNICO_DE_INFORMATICA = "Técnico de Informática"
    ENGENHARIA_DE_SOFTWARE = "Engenharia de Software"
    ENGENHARIA_DE_COMPUTACAO = "Engenharia de Computação"
    SISTEMAS_DE_INFORMACAO = "Sistemas de Informação"
    ANALISE_DESENVOLVIMENTO_DE_SISTEMAS = "Análise e Desenvolvimento de Sistemas"
    ENGENHARIA_DE_INFORMACAO = "Engenharia de Informação"
    CIENCIA_DA_COMPUTACAO = "Ciência da Computação"

class Aluno(Usuario):
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