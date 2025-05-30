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
            file_name: str,
            contents
    ):
        """
        Upload a file to Supabase storage.
        :param file_path: Path to the file to upload.
        :param file_name: Name of the file in Supabase storage.
        """
        response = self.client.storage.from_(self.bucket).upload(
            f"videoaulas/{file_name}",
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
            [f"videoaulas/{file_name}"]
        )
        return response

    async def get_video_url(self, video_url: str):
        """
        Get the public URL of a file in Supabase storage.
        :param file_name: Name of the file in Supabase storage.
        :return: Public URL of the file.
        """
        response = self.client.storage.from_(
            self.bucket
        ).get_public_url(video_url)
        return response
