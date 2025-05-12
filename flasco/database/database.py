from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from flasco.settings import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

DBsession = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_db():
    async with DBsession() as session:
        yield session
