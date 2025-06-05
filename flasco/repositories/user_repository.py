# import uuid
# from typing import Optional

# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.inspection import inspect

# from flasco.models.professor import Professor, FormacaoEnum
# from flasco.models.usuario import Usuario
# from flasco.repositories.base_repository import T, BaseRepository
# from flasco.application.dtos.auth_dto import ProfessorDTO, UserDTO


# class UserRepository(BaseRepository):
#     def __init__(self, db_session: AsyncSession):
#         super().__init__(db_session, Usuario)

#     async def get_user_by_id(self, id: uuid) -> Usuario:
#         query = select(Usuario).where(Usuario.id_usuario == id)
#         result = await self.db_session.execute(query)
#         return result.scalars().first()

#     async def create(self, item: T) -> T:
#         self.db_session.add(item)
#         await self.db_session.commit()
#         await self.db_session.refresh(item)

#         return item