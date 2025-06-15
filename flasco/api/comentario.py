from fastapi import APIRouter, Depends, Request, status
from flasco.application.dtos.comentario_dto import ComentarioDTO, ComentarioResponseDTO
from flasco.usecases.comentario.create_comentario import CreateComentarioUseCase
from flasco.usecases.comentario.get_comentarios_by_video import GetComentariosByVideo
from flasco.infra.middleware.verification_token_middleware import verification_token
from flasco.dependencies import (
    create_comentario_usecase,
    get_comentarios_by_video_usecase,
    swagger_security,
)

router = APIRouter(
    prefix="/comentario",
    tags=["Cometario"],
    dependencies=[Depends(swagger_security)]
)

@router.post("/create", status_code=status.HTTP_201_CREATED)
@verification_token
async def create_comentario(
    request: Request,
    comentario_data: ComentarioDTO,
    usecase: CreateComentarioUseCase = Depends(create_comentario_usecase)
):
    current_user = request.state.user
    comentario_data.id_usuario = current_user.user_id

    comentario_criado = await usecase.execute(comentario_data)
    return{
        "status": "sucesso",
        "comentario": comentario_criado
    }

@router.get("/video/{id_video}", response_model=list[ComentarioResponseDTO])
async def get_comentarios_video(
    id_video: str,
    usecase: GetComentariosByVideo = Depends(get_comentarios_by_video_usecase)
):
    comentarios = await usecase.execute(id_video)
    return comentarios
