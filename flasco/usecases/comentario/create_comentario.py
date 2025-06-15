from flasco.application.dtos.comentario_dto import ComentarioDTO, ComentarioResponseDTO
from flasco.repositories.comentario_repository import ComentarioRepository
from flasco.models.comentario import Comentario

class CreateComentarioUseCase:
    def __init__(self, repository: ComentarioRepository):
        self.repository = repository

    async def execute(self, comentario_dto: ComentarioDTO) -> ComentarioResponseDTO:
        comentario: Comentario = await self.repository.create(comentario_dto)

        return ComentarioResponseDTO(
            id_comentario=comentario.id_comentario,
            conteudo=comentario.conteudo,
            id_usuario=comentario.id_usuario,
            id_video=comentario.id_video,
            id_resposta=comentario.id_resposta
        )