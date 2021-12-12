from fastapi import FastAPI
from database.config import engine, Base
from routers.user_router import user_router
from routers.item_router import item_router
from routers.login_router import login_router
from routers.data_visualization import visualize_data

app = FastAPI()
app.include_router(user_router)
app.include_router(item_router)
app.include_router(login_router)


# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    import uvicorn

    app.mount("/dash", WSGIMiddleware(visualize_data().server))
    uvicorn.run(app, host="0.0.0.0", port=8000)
