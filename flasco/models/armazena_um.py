from uuid import UUID
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class ArmazenaUm:
    __tablename__ = "armazena_um"

    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("video.id_video"),
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
