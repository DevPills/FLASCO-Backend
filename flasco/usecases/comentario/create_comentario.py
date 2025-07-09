from flasco.application.dtos.comentario_dto import (
    ComentarioDTO,
    ComentarioResponseDTO
)
from flasco.repositories.comentario_repository import ComentarioRepository
from flasco.models.comentario import Comentario
from flasco.repositories.usuario_repository import UsuarioRepository
from flasco.usecases.auth.get_user_by_id import GetUserByIdUseCase


class CreateComentarioUseCase:
    def __init__(
        self,
        comentario_repository: ComentarioRepository,
        get_usuario_by_id_usecase: GetUserByIdUseCase,
        usuario_repository: UsuarioRepository
    ):
        self.comentario_repository = comentario_repository
        self.get_usuario_by_id_usecase = get_usuario_by_id_usecase
        self.usuario_repository = usuario_repository

    async def execute(
        self,
        comentario_dto: ComentarioDTO,
        current_user_email: str
    ) -> ComentarioResponseDTO:
        comentario: Comentario = await self.comentario_repository.create(
            comentario_dto
        )

        usuario = await self.usuario_repository.get_user_by_email(
            current_user_email
        )
        nome_usuario = usuario.nome

        return ComentarioResponseDTO(
            id_comentario=comentario.id_comentario,
            conteudo=comentario.conteudo,
            id_usuario=comentario.id_usuario,
            id_video=comentario.id_video,
            id_resposta=comentario.id_resposta,
            nome_usuario=nome_usuario,
        )