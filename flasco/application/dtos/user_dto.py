from pydantic import BaseModel


class UserResponseDTO(BaseModel):
    id_usuario: str
    nome: str
    email: str
    tipo: str
    instituicao: str | None = None
    created_at: str
    updated_at: str | None = None
