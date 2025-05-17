from uuid import uuid4, UUID
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import registry, mapped_column, Mapped


table_registry = registry()


@table_registry.mapped_as_dataclass
class Anexo:
    __tablename__ = "Anexo"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    tipo: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    anexo_path: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True,
    )
    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("video.id_video"),
        primary_key=True
    )
    id_anexo: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4
    )