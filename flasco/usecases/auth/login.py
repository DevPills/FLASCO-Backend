from fastapi import HTTPException, status
from flasco.application.dtos.auth_dto import LoginDTO
from flasco.application.utils.auth import verify_password
from flasco.infra