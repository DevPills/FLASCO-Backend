from uuid import UUID
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class FavoritaUm:
    __tablename__ = "favorita_um"

    id_modulo: Mapped[UUID] = mapped_column(
        ForeignKey("modulo.id_modulo"),
        primary_key=True,
    )
    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True,
    )
    estrela: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    modulo: Mapped["Modulo"] = relationship(
        back_populates="usuario_associado"
    )
    usuario: Mapped["Usuario"] = relationship(
        back_populates="modulo_associado"
    )