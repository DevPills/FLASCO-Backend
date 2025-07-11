from fastapi import Depends
from flasco.database.filestorage import SupabaseStorage
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from flasco.database.database import get_async_session
from flasco.repositories.aluno_repository import AlunoRepository
from flasco.repositories.armazena_um import ArmazenaUmRepository
from flasco.repositories.curte_um_repository import CurteUmRepository
from flasco.repositories.favorito_repository import FavoritoRepository
from flasco.repositories.modulo_repository import ModuloRepository
from flasco.repositories.professor_repository import ProfessorRepository
from flasco.repositories.usuario_repository import UsuarioRepository
from flasco.repositories.video_repository import VideoRepository
from flasco.repositories.comentario_repository import ComentarioRepository
from flasco.usecases.auth.create_user_aluno import CreateUserAlunoUseCase
from flasco.usecases.auth.create_user_professor import (
    CreateUserProfessorUseCase
)
from flasco.usecases.auth.delete_user import DeleteUserUseCase
from flasco.usecases.auth.get_user_by_id import GetUserByIdUseCase
from flasco.usecases.auth.login import LoginUseCase
from flasco.usecases.comentario.update_comentario import (
    UpdateComentarioUseCase
)
from flasco.usecases.dislike_video import DislikeVideoUseCase
from flasco.usecases.like_video import LikeVideoUseCase
from flasco.usecases.modulo.create_modulo_usecase import CreateModuloUseCase
from flasco.usecases.modulo.delete_modulo_usecase import DeleteModuloUseCase
from flasco.usecases.modulo.favorite_modulo_usecase import (
    FavoriteModuloUseCase
)
from flasco.usecases.modulo.get_all_modulos_usecase import GetAllModulosUseCase
from flasco.usecases.modulo.get_favorited_modulos_usecase import (
    GetFavoritedModulosUseCase
)
from flasco.usecases.user.get_current_user_details_usecase import (
    GetCurrentUserDetailsUseCase
)
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_get import GetVideoUseCase
from flasco.usecases.video_list import VideoListUseCase
from flasco.usecases.video_upload import VideoUploadUseCase
from flasco.usecases.comentario.get_comentarios_by_video import (
    GetComentariosByVideo
)
from flasco.usecases.comentario.create_comentario import (
    CreateComentarioUseCase
)
from flasco.usecases.comentario.delete_comentario import (
    DeleteComentarioUseCase
)

from sqlalchemy.ext.asyncio import AsyncSession
from flasco.settings import settings


def get_supabase_service() -> SupabaseStorage:
    return SupabaseStorage(
        bucket=settings.SUPABASE_BUCKET,
    )


def swagger_security(
        credentials: HTTPAuthorizationCredentials = Depends(
            HTTPBearer(auto_error=False)
        )
):
    return credentials


def get_video_repository(
    session: AsyncSession = Depends(get_async_session),
):
    return VideoRepository(db_session=session)


def usuario_repository(
    session: AsyncSession = Depends(get_async_session),
) -> UsuarioRepository:
    return UsuarioRepository(db_session=session)


def professor_repository(
    session: AsyncSession = Depends(get_async_session),
) -> ProfessorRepository:
    return ProfessorRepository(db_session=session)


def aluno_repository(
    session: AsyncSession = Depends(get_async_session),
) -> AlunoRepository:
    return AlunoRepository(db_session=session)


def modulo_repository(
    session: AsyncSession = Depends(get_async_session),
) -> ModuloRepository:
    return ModuloRepository(db_session=session)


def favorito_repository(
    session: AsyncSession = Depends(get_async_session),
) -> FavoritoRepository:
    return FavoritoRepository(db_session=session)


def comentario_repository(
    session: AsyncSession = Depends(get_async_session),
) -> ComentarioRepository:
    return ComentarioRepository(db_session=session)


def curte_um_repository(
    session: AsyncSession = Depends(get_async_session),
) -> CurteUmRepository:
    return CurteUmRepository(db_session=session)


def armazena_um_repository(
    session: AsyncSession = Depends(get_async_session),
) -> ArmazenaUmRepository:
    return ArmazenaUmRepository(db_session=session)


def create_professor_user_usecase(
    professor_repository: ProfessorRepository = Depends(professor_repository),
) -> CreateUserProfessorUseCase:
    return CreateUserProfessorUseCase(
        professor_repository=professor_repository
    )


def create_aluno_user_usecase(
    aluno_repository: AlunoRepository = Depends(aluno_repository),
) -> CreateUserAlunoUseCase:
    return CreateUserAlunoUseCase(aluno_repository=aluno_repository)


def delete_user_usecase(
    usuario_repository: UsuarioRepository = Depends(usuario_repository),
) -> DeleteUserUseCase:
    return DeleteUserUseCase(usuario_repository=usuario_repository)


def login_usecase(
    user_repository: UsuarioRepository = Depends(usuario_repository),
) -> LoginUseCase:
    return LoginUseCase(user_repository=user_repository)


def create_modulo_usecase(
    modulo_repository: ModuloRepository = Depends(modulo_repository),
) -> CreateModuloUseCase:
    return CreateModuloUseCase(modulo_repository=modulo_repository)


def favorite_module_usecase(
    favorito_repository: FavoritoRepository = Depends(favorito_repository),
) -> FavoriteModuloUseCase:
    return FavoriteModuloUseCase(
        favorito_repository=favorito_repository
    )


def delete_favorite_modulo_usecase(
    favorito_repository: FavoritoRepository = Depends(favorito_repository),
) -> DeleteModuloUseCase:
    return DeleteModuloUseCase(favorito_repository=favorito_repository)


def get_all_modulos_usecase(
    modulo_repository: ModuloRepository = Depends(modulo_repository),
) -> GetAllModulosUseCase:
    return GetAllModulosUseCase(modulo_repository=modulo_repository)


def get_favorited_modulos_usecase(
    modulo_repository: ModuloRepository = Depends(modulo_repository),
    favorito_repository: FavoritoRepository = Depends(favorito_repository),
) -> GetFavoritedModulosUseCase:
    return GetFavoritedModulosUseCase(
        modulo_repository=modulo_repository,
        favorito_repository=favorito_repository
    )


def video_upload_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
    armazena_um_repository: ArmazenaUmRepository = Depends(
        armazena_um_repository
    ),
) -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository,
        armazena_um_repository=armazena_um_repository
    )


def video_delete_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> DeleteVideoUseCase:
    return DeleteVideoUseCase(
        supabase_service=supabase_service,
        video_respository=video_repository
    )


def get_video_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> GetVideoUseCase:
    return GetVideoUseCase(
        video_repository=video_repository,
        supabase_service=supabase_service
    )


def list_video_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> VideoListUseCase:
    return VideoListUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository
    )


def get_usuario_by_id_usecase(
    usuario_repo: UsuarioRepository = Depends(usuario_repository),
) -> GetUserByIdUseCase:
    return GetUserByIdUseCase(repository=usuario_repo)


def create_comentario_usecase(
    comentario_repo: ComentarioRepository = Depends(comentario_repository),
    usuario_uc: GetUserByIdUseCase = Depends(get_usuario_by_id_usecase),
    usuario_repo: UsuarioRepository = Depends(usuario_repository),
) -> CreateComentarioUseCase:
    return CreateComentarioUseCase(
        comentario_repository=comentario_repo,
        get_usuario_by_id_usecase=usuario_uc,
        usuario_repository=usuario_repo
    )


def get_comentarios_by_video_usecase(
    comentario_repo: ComentarioRepository = Depends(comentario_repository),
) -> GetComentariosByVideo:
    return GetComentariosByVideo(comentario_repository=comentario_repo)


def delete_comentario_usecase(
    comentario_repo: ComentarioRepository = Depends(comentario_repository),
) -> DeleteComentarioUseCase:
    return DeleteComentarioUseCase(comentario_repository=comentario_repo)


def update_comentario_usecase(
    comentario_repo: ComentarioRepository = Depends(comentario_repository),
) -> UpdateComentarioUseCase:
    return UpdateComentarioUseCase(comentario_repository=comentario_repo)


def like_video_usecase(
    curte_um_repository: CurteUmRepository = Depends(curte_um_repository),
) -> LikeVideoUseCase:
    return LikeVideoUseCase(
        curte_um_repository=curte_um_repository
    )


def dislike_video_usecase(
    curte_um_repository: CurteUmRepository = Depends(curte_um_repository),
) -> DislikeVideoUseCase:
    return DislikeVideoUseCase(
        curte_um_repository=curte_um_repository
    )


def current_user_details_usecase(
    usuario_repository: UsuarioRepository = Depends(usuario_repository),
) -> GetCurrentUserDetailsUseCase:
    return GetCurrentUserDetailsUseCase(
        user_repository=usuario_repository
    )
