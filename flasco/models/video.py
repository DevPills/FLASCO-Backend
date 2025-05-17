from uuid import uuid4, UUID
from datetime import time
from sqlalchemy import Integer, String, Time, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship


table_registry = registry()


@table_registry.mapped_as_dataclass
class Video:
    __tablename__ = "video"

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

    modulo_associado: Mapped[list["ArmazenaUm"]] = relationship(
        back_populates="video",
        default_factory=list
    )

    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="video",
        cascade="all, delete-orphan",
        default_factory=list
    )




