import uuid
from pydantic import BaseModel

from flasco.application.enums.formacao import Formacao
from flasco.models.aluno import CursoEnum

class UserDTO(BaseModel):
    id: uuid.UUID
    nome: str
    instituicao: str
    email: str
    password: str

class ProfessorDTO(UserDTO):
    formacao: Formacao


class AlunoDTO(UserDTO): 
    curso: CursoEnum


class LoginDTO(BaseModel):
    email: str
    password: str

class CurrentUserDTO(BaseModel):
    user_id: str
    password: str