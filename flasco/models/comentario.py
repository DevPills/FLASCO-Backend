from uuid import uuid4, UUID
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from flasco.models.base import Base
from flasco.models.usuario import Usuario
from flasco.models.video import Video


class Comentario(Base):
    __tablename__ = "comentario"

    conteudo: Mapped[str] = mapped_column(
        String(400),
        nullable=False)
    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        nullable=False)
    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("videoaula.id_video"),
        nullable=False)
    id_resposta: Mapped[UUID | None] = mapped_column(
        ForeignKey("comentario.id_comentario"),
    )
    id_comentario: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default=uuid4)

    usuario: Mapped["Usuario"] = relationship(
        back_populates="comentarios")
    video: Mapped["Video"] = relationship(
        back_populates="comentarios")
    resposta_a: Mapped["Comentario | None"] = relationship(
        remote_side=[id_comentario],
        back_populates="respostas"
    )

    respostas: Mapped[list["Comentario"]] = relationship(
        back_populates="resposta_a",
        cascade="all, delete-orphan",
    )
