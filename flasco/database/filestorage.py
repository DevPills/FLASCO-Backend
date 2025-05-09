from supabase import acreate_client
from flasco.settings import settings

url: str = settings.SUPABASE_URL
key: str = settings.SUPABASE_ANON_KEY


class SupabaseStorage:
    def __init__(self, bucket: str):
        self.client = acreate_client(url, key)
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

        response = await self.client.storage.from_(self.bucket).upload(
            f"videoaulas/{file_name}",
            contents,
            file_options={
                "upsert": "true",
                "content-type": "video/mp4",
            }
        )
        return response
