from typing import TYPE_CHECKING
from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

if TYPE_CHECKING:
    from flasco.models.aluno import Aluno
    from flasco.models.professor import Professor
    from flasco.models.comentario import Comentario
    from flasco.models.favorita_um import FavoritaUm
    from flasco.models.curte_um import CurteUm
    from flasco.models.se_matricula import SeMatricula


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default=uuid4
    )
    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True)
    senha: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    instituicao: Mapped[str] = mapped_column(
        String(255),
        nullable=True)
    tipo: Mapped[str] = mapped_column(
        String(255),
        nullable=True)

    aluno: Mapped["Aluno"] = relationship(
        back_populates="usuario",
        uselist=False,  # Importante: indica que é um-para-um
        cascade="all, delete-orphan"
    )
    professor: Mapped["Professor"] = relationship(
        back_populates="usuario",
        uselist=False,  # Importante: indica que é um-para-um
        cascade="all, delete-orphan"
    )
    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
    )

    modulos_favoritados: Mapped[list["FavoritaUm"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
    )

    videos_curtidos: Mapped[list["CurteUm"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
    )

