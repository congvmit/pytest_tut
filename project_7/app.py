from contextlib import asynccontextmanager

from fastapi import FastAPI

# from pydantic import BaseModel
# from sqlalchemy import Column, Float, Integer, String, create_engine
# from sqlalchemy.ext.asyncio import AsyncSession
from db import DB_CONFIG, get_db, sessionmanager

# Base
# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     price = Column(Float, nullable=True)


# async def get_session():
#     session = Session()
#     try:
#         yield session
#     except Exception as e:
#         await session.rollback()
#         raise e
#     finally:
#         await session.commit()
#         await session.close()


# Schema
# class CreateItem(BaseModel):
#     name: str
#     description: str = None
#     price: float


# class GetItem(BaseModel):
#     id: int


def init_app(init_db=True):
    lifespan = None

    if init_db:
        sessionmanager.init(DB_CONFIG)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            if sessionmanager._engine is not None:
                async with sessionmanager.connect() as connection:
                    await sessionmanager.create_all(connection)
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    app = FastAPI(lifespan=lifespan)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    from views.items import router as items_router

    app.include_router(items_router)

    return app
