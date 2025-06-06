import uuid
from pydantic import BaseModel
from sqlalchemy import UUID


class ModuloDTO(BaseModel):
    nome: str 
    descricao: str
    id_professor_criador: uuid.UUID
 