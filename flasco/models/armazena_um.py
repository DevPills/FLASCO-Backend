from uuid import UUID
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

class ArmazenaUm(Base):
    __tablename__ = "armazena_um"

    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("videoaula.id_video"),
        primary_key=True)
    id_modulo: Mapped[UUID] = mapped_column(
        ForeignKey("modulo.id_modulo"),
        primary_key=True)
    posicao: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False)

    video: Mapped["Video"] = relationship(
        back_populates="modulos_associados")
    modulo: Mapped["Modulo"] = relationship(
        back_populates="videos_associados")
