from flasco.application.dtos.comentario_dto import ComentarioDTO, ComentarioResponseDTO
from flasco.repositories.comentario_repository import ComentarioRepository
from flasco.models.comentario import Comentario
from flasco.usecases.auth.get_user_by_id import GetUserByIdUseCase


class CreateComentarioUseCase:
    def __init__(
        self,
        comentario_repository: ComentarioRepository,
        get_usuario_by_id_usecase: GetUserByIdUseCase,
    ):
        self.comentario_repository = comentario_repository
        self.get_usuario_by_id_usecase = get_usuario_by_id_usecase

    async def execute(self, comentario_dto: ComentarioDTO) -> ComentarioResponseDTO:
        comentario: Comentario = await self.comentario_repository.create(comentario_dto)

        usuario = await self.get_usuario_by_id_usecase.execute(comentario.id_usuario)
        nome_usuario = usuario.nome

        return ComentarioResponseDTO(
            id_comentario=comentario.id_comentario,
            conteudo=comentario.conteudo,
            id_usuario=comentario.id_usuario,
            id_video=comentario.id_video,
            id_resposta=comentario.id_resposta,
            nome_usuario=nome_usuario,
        )