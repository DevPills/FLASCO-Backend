import enum
from uuid import UUID
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import registry, mapped_column, Mapped
from flasco.models.base_mixin import TimestampMixin

table_registry = registry()


class FormacaoEnum(enum.Enum):
    MESTRE = "Mestre"
    DOUTOR = "Doutor"
    PHD = "Ph.D."


@table_registry.mapped_as_dataclass
class Professor(TimestampMixin):
    __tablename__ = "professor"

    id_usuario: Mapped[UUID] = mapped_column(
        ForeignKey("usuario.id_usuario"),
        primary_key=True,
    )
    nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True)
    instituicao: Mapped[str] = mapped_column(
        String(255),
        nullable=False)
    formacao: Mapped[FormacaoEnum | None] = mapped_column(
        Enum(FormacaoEnum, name="formacao_enum", native_enum=True),
        nullable=True
    )
