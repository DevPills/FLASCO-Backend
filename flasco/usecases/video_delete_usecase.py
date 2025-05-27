from datetime import time
from http import HTTPStatus
import select
import uuid

from fastapi import HTTPException
from flasco.database import database
from flasco.database.database import AsyncSessionLocal
from flasco.database.filestorage import SupabaseStorage
from flasco.models.video import Video
from flasco.repositories.video_repository import VideoRepository


class DeleteVideoUseCase: 
    def __init__(
        self,
        supabase_service: SupabaseStorage,
        video_respository: VideoRepository,
    ):
        self.video_service = supabase_service
        self.video_respository = video_respository

    async def execute(self, video_name, paths, video_id):
        filestorage_delete = await self.video_service.remove(
            file_name=video_name,
            paths=paths
        )

        if not filestorage_delete:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Video nao existe"
            )

        database_delete = await self.video_respository.delete_video_by_id(
            video_id=video_id
        )

        if not database_delete:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Video nao existe"
            )

        return database_delete