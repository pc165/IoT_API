import asyncio
from typing import List
import dash
import dash_table
import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import parse_obj_as
from starlette.middleware.wsgi import WSGIMiddleware
from database import schemas
from database.config import async_session
from database.dal import DAL


async def prepare_data():
    async with async_session() as session:
        async with session.begin():
            db = DAL(session)
            data = await db.get_all_orders(skip=0, limit=100)
    data = parse_obj_as(List[schemas.Order], data)
    data = pd.DataFrame(jsonable_encoder(data))
    return data


def visualize_data():
    dash_app = dash.Dash(__name__, requests_pathname_prefix="/dash/")
    df1: pd.DataFrame = asyncio.run(prepare_data())
    df = df1.drop(columns="order_details")
    dash_app.layout = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
    )

    @dash_app.callback()
    def add_graph():
        return

    return dash_app


if __name__ == "__main__":
    server = FastAPI()
    server.mount("/dash", WSGIMiddleware(visualize_data().server))
    uvicorn.run(server)
