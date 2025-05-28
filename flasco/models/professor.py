import enum
from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship 
from flasco.models.usuario import Usuario

class FormacaoEnum(enum.Enum):
    MESTRE = "Mestre"
    DOUTOR = "Doutor"
    PHD = "Ph.D."


class Professor(Usuario):
    __tablename__ = "professor"

    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True,
    )

    formacao: Mapped[FormacaoEnum | None] = mapped_column(
        Enum(FormacaoEnum, name="formacao_enum", native_enum=True),
        nullable=True
    )

    modulos_criados: Mapped[list["Modulo"]] = relationship(
        back_populates="professor_criador",
        cascade="all, delete-orphan", 
    )

    usuario: Mapped["Usuario"] = relationship(
        back_populates="professor",
    )
