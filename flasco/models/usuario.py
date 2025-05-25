from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship
from flasco.models.base_mixin import TimestampMixin

table_registry = registry()


@table_registry.mapped_as_dataclass
class Usuario(TimestampMixin):
    __tablename__ = "usuario"

    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True)
    senha: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    instituicao: Mapped[str] = mapped_column(
        String(255), 
        nullable=True)
    id_usuario: Mapped[UUID] = mapped_column(
        Uuid(32), 
        primary_key=True,
        default_factory=uuid4
    )

    aluno: Mapped["Aluno"] = relationship(
        back_populates="usuario",
        uselist=False, # Importante: indica que é um-para-um
        cascade="all, delete-orphan" # Opcional: deleta o aluno se o usuario for deletado
    )
    professor: Mapped["Professor"] = relationship(
        back_populates="usuario",
        uselist=False, # Importante: indica que é um-para-um
        cascade="all, delete-orphan" # Opcional: deleta o professor se o usuario for deletado
    )
    comentarios: Mapped[list["Comentario"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
        default_factory=list
    )

    modulos_favoritados: Mapped[list["FavoritaUm"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
        default_factory=list
    )

    videos_curtidos: Mapped[list["CurteUm"]] = relationship(
        back_populates="usuario",
        cascade="all, delete-orphan",
        default_factory=list
    )

    matriculas: Mapped[list["SeMatricula"]] = relationship(
        back_populates="aluno",
        cascade="all, delete-orphan",
        default_factory=list
    )
