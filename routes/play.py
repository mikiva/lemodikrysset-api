from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
import json
from os import path

from supertokens_python.recipe.emailverification import EmailVerificationClaim
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session

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


@play.get("/puzzle/create")
async def create_for_verify(session: SessionContainer = Depends(verify_session())):
    print(session)
    return "OK"

@play.post("/puzzle/create")
async def create_for_verify_post(session: SessionContainer = Depends(verify_session())):
    print(session.__dict__)
    return "OK"

