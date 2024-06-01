from sys import modules

from sqlalchemy.ext.asyncio import create_async_engine

connection_url = (
    "sqlite+aiosqlite:///:memory:?cache=shared"
    if "pytest" in modules
    else "sqlite+aiosqlite:///tracking.db"
)

async_engine = create_async_engine(
    url=connection_url, future=True, connect_args={"check_same_thread": False}
)
