import uuid
from pydantic import BaseModel

from flasco.application.enums.curso import Curso
from flasco.application.enums.formacao import Formacao

class UserDTO(BaseModel):
    id: uuid.UUID
    nome: str
    instituicao: str
    email: str
    password: str

class ProfessorDTO(UserDTO):
    formacao: Formacao


class AlunoDTO(UserDTO): 
    curso: Curso


class LoginDTO(BaseModel):
    email: str
    password: str

class CurrentUserDTO(BaseModel):
    user_id: str
    password: str