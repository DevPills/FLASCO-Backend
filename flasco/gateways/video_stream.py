import httpx


class VideoStreamGateway:
    """
    Class to handle video streaming from a given URL.
    """
    @staticmethod
    async def start_stream(video_url: str):
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "GET", video_url, headers={'Range': 'bytes=0-'}, timeout=None
            ) as response:
                async for chunk in response.aiter_bytes():
                    yield chunk
