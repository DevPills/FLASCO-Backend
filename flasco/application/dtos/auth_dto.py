from pydantic import BaseModel

class CreateUserDTO(BaseModel):
    email: str
    password: str

class CreateProfessorDTO(CreateUserDTO):
    pru: str

class CreateAlunoDTO(CreateUserDTO):
    pru: str


class LoginDTO(BaseModel):
    email: str
    password: str

class CurrentUserDTO(BaseModel):
    user_id: str
    password: str