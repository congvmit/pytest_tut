import asyncio
from contextlib import ExitStack

import pytest
import pytest_asyncio
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app import init_app
from db import Base, get_db, sessionmanager

# import sys
# sys.path.append("..") # Use pytest.ini instead


@pytest.fixture(autouse=True, scope="session")
def app():
    with ExitStack():
        app = init_app(init_db=False)
        yield app


@pytest.fixture
def client(app):
    print("> Fixture: Creating client")

    async def get_db_override():
        async with sessionmanager.session() as session:
            yield session

    app.dependency_overrides[get_db] = get_db_override

    # Method 1: Using TestClient from fastapi.testclient
    # This helps automatically call lifespan events on the FastAPI app
    with TestClient(app=app, base_url="http://test") as c:
        yield c

    # Method 2: Using AsyncClient from httpx
    # Cons:
    # - Does not call lifespan events on the FastAPI app
    # async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as c:
    #     yield c


# @pytest.fixture(scope="session")
# def event_loop(request):
#     # loop = asyncio.get_event_loop_policy().new_event_loop()
#     loop = asyncio.get_running_loop()
#     yield loop
#     loop.close()

# event_loop
# Scope can be: function, class, module, package or session
# function: run once per test function
# class: run once per test class
# module: run once per module
# package: run once per package
# session: run once per session


@pytest_asyncio.fixture(scope="session", autouse=True)
async def connection_test():
    print("> Session: Initializing database")
    sessionmanager.init("sqlite+aiosqlite:///:memory:")
    async with sessionmanager.session() as session:
        async with session.begin():
            yield session
        await sessionmanager.close()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def create_tables(connection_test):
    print("> Function: Creating tables")
    async with sessionmanager.connect() as connection:
        await sessionmanager.drop_all(connection)
        await sessionmanager.create_all(connection)


async def get_db_override():
    async with sessionmanager.session() as session:
        yield session


# @pytest_asyncio.fixture(scope="function", autouse=True)
# async def session_override(app, connection_test):
#     print("> Function: Overriding get_db")
#     app.dependency_overrides[get_db] = get_db_override
