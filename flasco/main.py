from fastapi import FastAPI
from flasco.api.video import router as video_router
from flasco.api.auth import router as auth_router
from flasco.api.modulo import router as modulo_router
from flasco.api.enums import router as enum_router
from flasco.api.comentario import router as comentario_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

app = FastAPI()

security = HTTPBearer()

app.include_router(auth_router)
app.include_router(video_router)
app.include_router(modulo_router)
app.include_router(auth_router) 
app.include_router(enum_router)
app.include_router(comentario_router)

origins = [
    "https://flasco.dev.br",
    "http://localhost:3000/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
