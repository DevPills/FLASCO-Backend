from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base_timestamp import TimestampBase
from flasco.models.base import Base

class Usuario(Base, TimestampBase):
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

    aluno: Mapped["Aluno"] = relationship(
        back_populates="usuario",
        uselist=False, # Importante: indica que é um-para-um
        cascade="all, delete-orphan" # Opcional: deleta o aluno se o usuario for deletado
    )
    professor: Mapped["Professor"] = relationship(
        back_populates="usuario",
        uselist=False, # Importante: indica que é um-para-um
        cascade="all, delete-orphan" # Opcional: deleta o professor se o usuario for deletado
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

    matriculas: Mapped[list["SeMatricula"]] = relationship(
        back_populates="aluno",
        cascade="all, delete-orphan",
    )
