from pydantic import BaseModel


class LikeVideoDTO(BaseModel):
    id_video: str
    id_usuario: str

    class Config:
        orm_mode = True
