import enum
from uuid import uuid4, UUID
from sqlalchemy import String, Uuid
from sqlalchemy.orm import registry, mapped_column, Mapped

table_registry = registry()


class CursoEnum(enum.Enum):
    TECNICO_DE_INFORMATICA = "Técnico de Informática",
    ENGENHARIA_DE_SOFTWARE = "Engenharia de Software",
    ENGENHARIA_DE_COMPUTACAO = "Engenharia de Computação",
    SISTEMAS_DE_INFORMACAO = "Sistemas de Informação",
    ANALISE_DESENVOLVIMENTO_DE_SISTEMAS = "Analise e Desenvolvimento de Sistemas",
    ENGENHARIA_DE_INFORMACAO = "Engenharia de Informação",
    CIENCIA_DA_COMPUTACAO = "Ciência Da Computação"


@table_registry.mapped_as_dataclass
class Aluno:
    __tablename__ = "Aluno"

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
    curso: Mapped[CursoEnum | None] = mapped_column(
        Enum(CursoEnum, name="curso_enum", native_enum=True),
        nullable=True
    )