import uuid
from pydantic import BaseModel


class ModuloDTO(BaseModel):
    nome: str
    descricao: str
    
class CreateModuloDTO(BaseModel):
    nome: str
    descricao: str
    id_professor_criador: uuid.UUID

class FavoriteModuloDTO(BaseModel):
    id_modulo: str
    id_usuario: str


class FavoriteModuloResponseDTO(BaseModel):
    status: str
    message: str


class GetModuloDTO(BaseModel):
    id_modulo: uuid.UUID
    nome: str
    descricao: str


class ArmazenaUmDTO(BaseModel):
    id_video: uuid.UUID
    id_modulo: uuid.UUID
    posicao: int
