from contextlib import asynccontextmanager

from db import DB_CONFIG, sessionmanager
from fastapi import FastAPI


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
    from views.users import router as users_router

    app.include_router(items_router)
    app.include_router(users_router)

    return app
