from typing import Any
from supabase import create_client
from flasco.settings import settings
import uuid

url: str = settings.SUPABASE_URL
key: str = settings.SUPABASE_ANON_KEY


class SupabaseStorage:
    def __init__(self, bucket: str):
        self.client = create_client(url, key)
        self.bucket = bucket

    async def upload(
            self,
            file_name: str,
            contents
    ):
        """
        Upload a file to Supabase storage.
        :param file_path: Path to the file to upload.
        :param file_name: Name of the file in Supabase storage.
        """
        unique_name = uuid.uuid4()

        response = self.client.storage.from_(self.bucket).upload(
            f"videoaulas/{file_name}",
            f"videoaulas/{unique_name}",
            contents,
            file_options={
                "upsert": "true",
                "content-type": "video/mp4",
            }
        )
        return response
    

    async def remove(
           self, 
           file_name: str,
           paths: str
    ):
        response = self.client.storage.from_(self.bucket).remove(
            [f"{paths}{file_name}"]
        )
        return response