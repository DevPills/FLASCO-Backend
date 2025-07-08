from fastapi import APIRouter, Depends, Request, status

from flasco.dependencies import current_user_details_usecase
from flasco.infra.middleware.verification_token_middleware import (
    verification_token
)
from flasco.usecases.user.get_current_user_details_usecase import (
    GetCurrentUserDetailsUseCase
)

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", status_code=status.HTTP_200_OK)
@verification_token
async def get_current_user_details(
    request: Request,
    usecase: GetCurrentUserDetailsUseCase = Depends(
        current_user_details_usecase
    )
):
    current_user = request.state.user

    user = await usecase.execute(current_user.user_id)
    return user
