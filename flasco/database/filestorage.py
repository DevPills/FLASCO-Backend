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
    
    async def list_files(
        self,
        prefix: str = "videoaulas",  
        limit: int | None = None,
        offset: int = 0,
    ):
        """
        List of objects in the bucket. We omit limit/offset when not needed.
        """

        options: dict = {}
        if limit is not None:        
            options["limit"] = limit
        if offset:                     
            options["offset"] = offset

        objects = self.client.storage.from_(self.bucket).list(
            path=prefix,
            options=options or None
        )

        file_list = []
        for obj in objects:
            file_path = f"{prefix}/{obj['name']}" if prefix else obj["name"]
            public_url = self.client.storage.from_(self.bucket).get_public_url(
                file_path
            )
            file_list.append(
                {
                    "name": obj["name"],
                    "path": file_path,
                    "size": obj["metadata"].get("size"),
                    "updated_at": obj["updated_at"],
                    "url": public_url,
                }
            )
        return file_list
