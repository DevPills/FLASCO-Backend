from uuid import uuid4, UUID
from datetime import time
from sqlalchemy import Integer, String, Time, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped


tabble_registry = registry()


@tabble_registry.mapped_as_dataclass
class Video:
    __tablename__ = "videoaula"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    descricao: Mapped[str] = mapped_column(
        String(500),
    )
    duracao: Mapped[time] = mapped_column(
        Time,
        nullable=False,
    )
    videoaula_path: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    id_professor: Mapped[UUID] = mapped_column(
        Uuid(32),
        nullable=False
    )
    id_video: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4
    )
    qntd_curtidas: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )
