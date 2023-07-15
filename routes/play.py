from typing import Union

from bson import ObjectId
from fastapi import APIRouter, Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
import json
from os import path

from pydantic import create_model
from supertokens_python.recipe.emailverification import EmailVerificationClaim
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session

from dependencies import puzzle_service_provider
from models import Puzzle, PuzzleExtended
from services.puzzleservice import PuzzleService

play = APIRouter(prefix="/play")


@play.get("/puzzle", response_model=PuzzleExtended | Puzzle, response_model_exclude={"id"},
          response_model_exclude_unset=True)
async def get_puzzle(p: str,
                     puzzle_service: PuzzleService = Depends(puzzle_service_provider),
                     session: SessionContainer = Depends(
                         verify_session(session_required=False))) -> PuzzleExtended | Puzzle:
    puzzle = await puzzle_service.get_puzzle(p)
    extended = False
    if session is not None:
        s = session.get_user_id()
        creator = puzzle.get("metadata", {}).get("createdBy")
        extended = creator == s

    if extended:
        return PuzzleExtended(**puzzle)
    else:
        return Puzzle(**puzzle)


@play.get("/puzzle/exists")
async def get_puzzle_exists(p: str, puzzle_service: PuzzleService = Depends(puzzle_service_provider)):
    # puzzle_id = p.casefold()
    # exists = path.exists(f"routes/{puzzle_id}.json")
    exists = await puzzle_service.puzzle_exists(p.casefold())
    if not exists:
        return Response(status_code=404)

    return Response(status_code=204)


@play.get("/puzzle/create")
async def create_for_verify(request: Request, session: SessionContainer = Depends(verify_session())):
    return "OK"


@play.post("/puzzle/create")
async def create_for_verify_post(request: Request, session: SessionContainer = Depends(verify_session())):
    print(session.__dict__)
    data = await request.json()
    print(data)
    return "OK"
