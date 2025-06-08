from fastapi import Depends
from flasco.database.filestorage import SupabaseStorage
from flasco.database.database import get_async_session
from flasco.repositories.aluno_repository import AlunoRepository
from flasco.repositories.favorito_repository import FavoritoRepository
from flasco.repositories.modulo_repository import ModuloRepository
from flasco.repositories.professor_repository import ProfessorRepository
from flasco.repositories.usuario_repository import UsuarioRepository
from flasco.repositories.video_repository import VideoRepository
from flasco.usecases.auth.create_user_aluno import CreateUserAlunoUseCase
from flasco.usecases.auth.create_user_professor import (
    CreateUserProfessorUseCase
)
from flasco.usecases.auth.login import LoginUseCase
from flasco.usecases.modulo.create_modulo_usecase import CreateModuloUseCase
from flasco.usecases.video_delete_usecase import DeleteVideoUseCase
from flasco.usecases.video_get import GetVideoUseCase
from flasco.usecases.video_list import VideoListUseCase
from flasco.usecases.video_upload import VideoUploadUseCase
from sqlalchemy.ext.asyncio import AsyncSession
from flasco.settings import settings


def get_supabase_service() -> SupabaseStorage:
    return SupabaseStorage(
        bucket=settings.SUPABASE_BUCKET,
    )


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


def login_usecase(
    user_repository: UsuarioRepository = Depends(usuario_repository),
) -> LoginUseCase:
    return LoginUseCase(user_repository=user_repository)


def create_modulo_usecase(
    modulo_repository: ModuloRepository = Depends(modulo_repository),
) -> CreateModuloUseCase:
    return CreateModuloUseCase(modulo_respoitory=modulo_repository)


def video_upload_usecase(
    video_repository: VideoRepository = Depends(get_video_repository),
    supabase_service: SupabaseStorage = Depends(get_supabase_service),
) -> VideoUploadUseCase:
    return VideoUploadUseCase(
        supabase_service=supabase_service,
        video_repository=video_repository
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
