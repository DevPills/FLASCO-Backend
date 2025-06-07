from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.pool import NullPool
from flasco.settings import settings

ca_path = '/home/alexandre/FLASCO-Backend/prod-ca-2021.crt'

database_url = settings.DATABASE_URL.replace('postgresql+asyncpg://', 'postgresql+psycopg://')

engine = create_async_engine(
    database_url,
    connect_args={
        "sslmode": "verify-full",
        "sslrootcert": ca_path
    },
    poolclass=NullPool,
    echo=True
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False
)

async def get_async_session():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()