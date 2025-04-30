from fastapi import UploadFile
from supabase import create_client
from flasco.settings import settings

url: str = settings.SUPABASE_URL
key: str = settings.SUPABASE_ANON_KEY


class SupabaseStorage:
    def __init__(self, bucket: str):
        self.client = create_client(url, key)
        self.bucket = bucket

    async def upload(
            self,
            file: UploadFile,
            file_name: str,
            content_type: str = None
    ):
        """
        Upload a file to Supabase storage.
        :param file_path: Path to the file to upload.
        :param file_name: Name of the file in Supabase storage.
        """

        contents = file.read()
        response = self.client.storage.from_(self.bucket).upload(
            path=f"videoaulas/{file_name}",
            file=contents,
            file_options={
                "content_type": "application/octet-stream",
                "upsert": "true",
            }
        )
        return response
