from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Modulo:
    __tablename__ = "modulo"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    descricao: Mapped[str] = mapped_column(
        String(500)
    )
    id_modulo: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4
    )
    modulo_associado: Mapped[list["ArmazenaUm"]] = relationship(
        back_populates="modulo",
        default_factory=list
    )
    favoritos: Mapped[list["FavoritaUm"]] = relationship(
        back_populates="modulo",
        cascade="all, delete-orphan",
        default_factory=list
    )

