import enum
from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped

table_registry = registry()


class FormacaoEnum(enum.Enum):
    MESTRE = "Mestre",
    DOUTOR = "Doutor",
    PHD = "Ph.D."


@table_registry.mapped_as_dataclass
class Professor:
    __tablename__ = "Professor"

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
        nullable=False,
    )
    id_usuario: Mapped[UUID] = mapped_column(
        Uuid(32),
        primary_key=True,
        default_factory=uuid4
    )
    curso: Mapped[CursoEnum | None] = mapped_column(
        Enum(FormacaoEnum, name="formacao_enum", native_enum=True),
        nullable=True
    )