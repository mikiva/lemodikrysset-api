from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
import json
from os import path
play = APIRouter(prefix="/play")


@play.get("/puzzle")
async def get_puzzle(p: str):
    with open(f"routes/{p}.json") as test:
        data = json.load(test)

    return JSONResponse(data)

@play.get("/puzzle/exists")
async def get_puzzle_exists(p: str):
    puzzle_id = p.casefold()
    exists = path.exists(f"routes/{puzzle_id}.json")
    if not exists:
        return Response(status_code=404)
    return Response(status_code=204)
