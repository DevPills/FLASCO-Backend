import enum
from uuid import UUID
from sqlalchemy import String, Enum, ForeignKey
from sqlalchemy.orm import registry, mapped_column, Mapped, relationship
from flasco.models.base_mixin import TimestampMixin

table_registry = registry()


class CursoEnum(enum.Enum):
    TECNICO_DE_INFORMATICA = "Técnico de Informática"
    ENGENHARIA_DE_SOFTWARE = "Engenharia de Software"
    ENGENHARIA_DE_COMPUTACAO = "Engenharia de Computação"
    SISTEMAS_DE_INFORMACAO = "Sistemas de Informação"
    ANALISE_DESENVOLVIMENTO_DE_SISTEMAS = "Análise e Desenvolvimento de Sistemas"
    ENGENHARIA_DE_INFORMACAO = "Engenharia de Informação"
    CIENCIA_DA_COMPUTACAO = "Ciência da Computação"


@table_registry.mapped_as_dataclass
class Aluno(TimestampMixin):  # Se quiser timestamps, mantenha
    __tablename__ = "aluno"

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
        nullable=True)
    curso: Mapped[CursoEnum | None] = mapped_column(
        Enum(CursoEnum,name="curso_enum", native_enum=True),
        nullable=True
    )

    modulos_matriculados: Mapped[list["SeMatricula"]] = relationship(
        back_populates="aluno",
        cascade="all, delete-orphan",
        default_factory=list
    )
