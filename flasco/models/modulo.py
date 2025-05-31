from typing import TYPE_CHECKING
from uuid import uuid4, UUID
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

if TYPE_CHECKING:
    from flasco.models.professor import Professor
    from flasco.models.armazena_um import ArmazenaUm
    from flasco.models.favorita_um import FavoritaUm
    from flasco.models.se_matricula import SeMatricula


class Modulo(Base):
    __tablename__ = "modulo"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    descricao: Mapped[str] = mapped_column(
        String(500),
        nullable=True)
    id_professor_criador: Mapped[UUID] = mapped_column(
        ForeignKey("professor.id_usuario"),
        nullable=False
    )
    id_modulo: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default=uuid4
    )

    professor_criador: Mapped["Professor"] = relationship(
            back_populates="modulos_criados"
        )
    videos_associados: Mapped[list["ArmazenaUm"]] = relationship(
        back_populates="modulo",
    )

    modulos_favoritados: Mapped[list["FavoritaUm"]] = relationship(
        back_populates="modulo",
        cascade="all, delete-orphan",
    )

    alunos_matriculados: Mapped[list["SeMatricula"]] = relationship(
        back_populates="modulo",
        cascade="all, delete-orphan",
    )
