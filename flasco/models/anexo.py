from uuid import uuid4, UUID
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base
from flasco.models.video import Video


class Anexo(Base):
    __tablename__ = "anexo"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    tipo: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    anexo_path: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True)
    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("videoaula.id_video"),
        nullable=False)
    id_anexo: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default=uuid4)

    video: Mapped["Video"] = relationship(
        back_populates="anexos")
