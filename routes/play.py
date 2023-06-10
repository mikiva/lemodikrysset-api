from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json

play = APIRouter(prefix="/play")


@play.get("/puzzle")
async def get_puzzle(p: str):
    with open(f"routes/{p}.json") as test:
        data = json.load(test)

    return JSONResponse(data)
