import jwt
from functools import wraps
from http import HTTPStatus
from flasco.application.dtos.auth_dto import CurrentUserDTO
from flasco.application.dtos.error_dto import ServiceError
from flasco.settings import settings


def verification_token(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get("request")
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return ServiceError(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                message="Token inválido ou não fornecido"
            )
        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return ServiceError(
                status_code=HTTPStatus.UNAUTHORIZED,
                message="Token expirado."
            )
        except jwt.InvalidTokenError:
            raise ServiceError(
                status_code=HTTPStatus.UNAUTHORIZED,
                message="Token inválido"
            )
        request.state.user = CurrentUserDTO(
            user_id=payload.get("user_id"),
            email=payload.get("email")
        )
        return await func(*args, **kwargs)
    return wrapper
