from sqlalchemy import select
from flasco.models import User
from http import HTTPStatus
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import TypeVar


T = TypeVar("T")


class UserRepository: 
    def __init__(self, db_session: AssertionError):
        