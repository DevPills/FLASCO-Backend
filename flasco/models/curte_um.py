from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base
from flasco.models.usuario import Usuario
from flasco.models.video import Video


class CurteUm(Base):
    __tablename__ = "curte_um"

    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True)
    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("videoaula.id_video"),
        primary_key=True)

    usuario: Mapped["Usuario"] = relationship(
        back_populates="videos_curtidos")
    video: Mapped["Video"] = relationship(
        back_populates="curtidas")
