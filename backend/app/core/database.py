import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv



load_dotenv()
URI_DATABASE = os.getenv('URI_DATABASE')

engine = create_async_engine(URI_DATABASE, echo=False)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# ⬇️ Função para criar tabelas
async def init_db():
    import app.models.user
    import app.models.event
    import app.models.attendance
    #import app.models.location

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)