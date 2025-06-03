from typing import Optional
import uuid
from pydantic import BaseModel

from flasco.application.enums.curso import Curso
from flasco.application.enums.formacao import Formacao

class UserDTO(BaseModel):
    nome: str
    instituicao: str
    email: str
    senha: str
    tipo: str

class ProfessorDTO(UserDTO):
    formacao: Formacao


class AlunoDTO(UserDTO): 
    curso: Curso


class LoginDTO(BaseModel):
    email: str
    senha: str

class CurrentUserDTO(BaseModel):
    user_id: str
    senha: str