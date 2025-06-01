from fastapi import FastAPI
from flasco.api.video import router as video_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(video_router)

origins = [
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
