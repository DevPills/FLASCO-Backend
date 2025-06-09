from pydantic import BaseModel


class ModuloDTO(BaseModel):
    nome: str
    descricao: str
