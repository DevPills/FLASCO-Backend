from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship    

table_registry = registry()


@table_registry.mapped_as_dataclass
class Usuario:
    __tablename__ = "Usuario"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    instituicao: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    id_usuario: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4
    )

    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
        default_factory=list
    )

    favoritos: Mapped[list["FavoritaUm"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
        default_factory=list
    )

