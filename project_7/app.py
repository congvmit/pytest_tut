from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True, future=True)
Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=True)


async def get_session():
    session = Session()
    try:
        yield session
    except Exception as e:
        await session.rollback()
        raise e
    finally:
        await session.commit()
        await session.close()


# Schema
class CreateItem(BaseModel):
    name: str
    description: str = None
    price: float


class GetItem(BaseModel):
    id: int


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with engine.begin() as conn:
#         print(">> Creating tables")
#         await conn.run_sync(Base.metadata.create_all)
#         yield


def init_app(init_db=True):
    lifespan = None

    if init_db:

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            async with engine.begin() as conn:
                print(">> Creating tables")
                await conn.run_sync(Base.metadata.create_all)
                yield

    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.post("/items/")
    async def create_item(item: CreateItem, session: AsyncSession = Depends(get_session)):
        try:
            new_item = Item(name=item.name, description=item.description, price=item.price)
            session.add(new_item)
            await session.commit()
        except Exception as e:
            return {"message": "internal error", "data": {}}
        else:
            return {"message": "success", "data": item.model_dump()}

    @app.get("/items/{id}")
    async def get_item(id: str, session: AsyncSession = Depends(get_session)):
        try:
            item = await session.get(Item, id)
            if item is None:
                return {"message": "success", "data": {}}
            else:
                return {
                    "message": "success",
                    "data": {
                        "name": item.name,
                        "description": item.description,
                        "price": item.price,
                    },
                }
        except Exception as e:
            return {"message": f"internal error {e}", "data": {}}

    return app
