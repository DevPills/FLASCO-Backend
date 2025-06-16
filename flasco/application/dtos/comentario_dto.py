from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from uuid import UUID


class ComentarioDTO(BaseModel):
    conteudo: str
    id_usuario: UUID
    id_video: UUID
    id_resposta: Optional[UUID] = None 


class ComentarioResponseDTO(BaseModel):
    id_comentario: UUID
    conteudo: str
    id_usuario: UUID
    id_video: UUID
    id_resposta: Optional[UUID] = None

