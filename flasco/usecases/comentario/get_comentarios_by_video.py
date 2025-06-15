from typing import List
from flasco.application.dtos.comentario_dto import ComentarioResponseDTO
from flasco.repositories.comentario_repository import ComentarioRepository

class GetComentariosByVideo:
    def __init__(self, comentario_repository: ComentarioRepository):
        self.comentario_repository = comentario_repository

    async def execute(self, id_video: str) -> List[ComentarioResponseDTO]:
        comentarios = await self.comentario_repository.get_comentarios_by_video_id(id_video)
        return [
            ComentarioResponseDTO.model_validate({
             "id_comentario": comentario.id_comentario,
                "conteudo": comentario.conteudo,
                "id_usuario": comentario.id_usuario,
                "id_video": comentario.id_video,
                "id_resposta": comentario.id_resposta
            })
            for comentario in comentarios
        ]
