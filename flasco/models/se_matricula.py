from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

if TYPE_CHECKING:
    from flasco.models.aluno import Aluno
    from flasco.models.modulo import Modulo


class SeMatricula(Base):
    __tablename__ = "se_matricula"

    id_aluno: Mapped[UUID] = mapped_column(
        ForeignKey("aluno.id_usuario"),
        primary_key=True
    )
    id_modulo: Mapped[UUID] = mapped_column(
        ForeignKey("modulo.id_modulo"),
        primary_key=True
    )

    aluno: Mapped["Aluno"] = relationship(
        back_populates="modulos_matriculados")
    modulo: Mapped["Modulo"] = relationship(
        back_populates="alunos_matriculados")
