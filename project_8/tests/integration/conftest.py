import asyncio
import sys
from contextlib import ExitStack

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.testing.entities import ComparableEntity

sys.path.append("..")
from app import init_app
from app.models import User
from app.services.database import get_db, sessionmanager


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        app = init_app(init_db=False)
        yield app


@pytest.fixture
def client(app):
    with TestClient(app=app) as c:
        yield c


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def connection_test(event_loop):
    sessionmanager.init("sqlite:///:memory:")  # +aiosqlite
    async with sessionmanager() as session:
        async with session.begin():
            yield session
        await sessionmanager.close()


@pytest.fixture(scope="function", autouse=True)
async def create_tables(connection_test):
    async with sessionmanager.connect() as connection:
        await sessionmanager.drop_all(connection)
        await sessionmanager.create_all(connection)


@pytest.fixture(scope="function", autouse=True)
async def session_override(app, connection_test):
    async def get_db_override():
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_db_override

    # return app
