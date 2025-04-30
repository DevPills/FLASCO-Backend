from fastapi import FastAPI
from flasco.api.video import router as video_router

app = FastAPI()

app.include_router(video_router)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
