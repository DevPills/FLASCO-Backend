from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base

class FavoritaUm(Base):
    __tablename__ = "favorita_um"

    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True)
    id_modulo: Mapped[UUID] = mapped_column(
        ForeignKey("modulo.id_modulo"),
        primary_key=True)

    usuario: Mapped["Usuario"] = relationship(
        back_populates="modulos_favoritados")
    modulo: Mapped["Modulo"] = relationship(
        back_populates="modulos_favoritados")
