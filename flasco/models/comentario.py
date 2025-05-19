from uuid import uuid4, UUID
from sqlalchemy import String, Uuid, ForeignKey
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship
from flasco.models.base_mixin import TimestampMixin

table_registry = registry()


@table_registry.mapped_as_dataclass
class Comentario(TimestampMixin):
    __tablename__ = "comentario"

    id_comentario: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4)
    conteudo: Mapped[str] = mapped_column(
        String(400),
        nullable=False)
    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        nullable=False)
    id_video: Mapped[UUID] = mapped_column(
        ForeignKey("video.id_video"),
        nullable=False)
    id_resposta: Mapped[UUID | None] = mapped_column(
        ForeignKey("comentario.id_comentario"),
        nullable=True
    )

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
        default_factory=list
    )
