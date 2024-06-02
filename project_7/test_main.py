import pytest
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, declarative_base, async_sessionmaker
from project_7.app import CreateItem
from contextlib import ExitStack


@pytest.fixture
def app():
    from project_7.app import init_app
    app = init_app(init_db=False)
    
    return app

# @pytest.fixture(scope="function")
# def session():
#     Base = declarative_base()
#     engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True, future=True)
#     Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

#     return get_session()


# Method 1: Using TestClient from fastapi.testclient
@pytest.mark.asyncio
async def test_root(app):
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


# Method 2: Using AsyncClient from httpx
@pytest.mark.asyncio
async def test_root_2(app):
    async with AsyncClient(base_url="http://test", transport=ASGITransport(app=app)) as client:
        response = await client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_create_item(app):
    with TestClient(app=app, base_url="http://test") as client:
        response = client.post(
            "/items/",
            json={"name": "item1", "description": "description1", "price": 9.99},
        )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {"name": "item1", "description": "description1", "price": 9.99},
    }


@pytest.mark.asyncio
async def test_get_item_found(app):
    with TestClient(app=app, base_url="http://test") as client:
        response = client.post(
            "/items/",
            json={"name": "item2", "description": "description2", "price": 9.99},
        )

        response = client.get("/items/2")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {"name": "item2", "description": "description2", "price": 9.99},
    }


@pytest.mark.asyncio
async def test_get_item_not_found(app):
    with TestClient(app=app, base_url="http://test") as client:
        response = client.get("/items/3")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "success",
        "data": {},
    }
