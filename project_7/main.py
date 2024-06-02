from app import init_app

app = init_app(init_db=True)

# # DEBUG
# import mipkit;mipkit.debug.set_trace();exit();


# async def common_parameters(
#     q = None, skip: int = 0, limit: int = 100
# ):
#     return {"q": q, "skip": skip, "limit": limit}

# async def override_dependency(q=None):
#     return {"q": q, "skip": 5, "limit": 10}

# app.dependency_overrides[common_parameters] = override_dependency
