from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class ClassUm:
    __tablename__ = "curte_um"

    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("video.id_video"),
        primary_key=True
    )
    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True
    )

    video: Mapped["Video"] = relationship(
        back_populates="usuario_associado"
    )
    usuario: Mapped["Usuario"] = relationship(
        back_populates="video_associado"
    )