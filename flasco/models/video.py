from typing import TYPE_CHECKING
from uuid import uuid4, UUID
from datetime import time
from sqlalchemy import Integer, String, Time, Uuid, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

if TYPE_CHECKING:
    from flasco.models.armazena_um import ArmazenaUm
    from flasco.models.comentario import Comentario
    from flasco.models.curte_um import CurteUm
    from flasco.models.favorita_um import FavoritaUm
    from flasco.models.anexo import Anexo


class Video(Base):
    __tablename__ = "videoaula"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    descricao: Mapped[str] = mapped_column(
        String(500))
    duracao: Mapped[time] = mapped_column(
        Time,
        nullable=False)
    videoaula_path: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    id_professor: Mapped[UUID] = mapped_column(
        ForeignKey("professor.id_usuario"),
        nullable=False)
    qntd_curtidas: Mapped[int] = mapped_column(
        Integer,
        default=0)

    modulos_associados: Mapped[list["ArmazenaUm"]] = relationship(
        back_populates="video"
    )
    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="video",
        cascade="all, delete-orphan",
    )
    curtidas: Mapped[list["CurteUm"]] = relationship(
        back_populates="video",
        cascade="all, delete-orphan",
    )
    anexos: Mapped[list["Anexo"]] = relationship(
        back_populates="video",
        cascade="all, delete-orphan",
    )
    id_video: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default=uuid4)
