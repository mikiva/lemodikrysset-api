from fastapi import FastAPI, status, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from auth import init_auth
from settings import AuthSettings
from supertokens_python import get_all_cors_headers
from routes.play import play
from database import init_database, close_database

settings = AuthSettings()
app = FastAPI()
app.include_router(play, prefix="/api/v1")

init_auth(app)



@app.on_event("startup")
async def app_startup():
    await init_database()
@app.on_event("shutdown")
async def app_shutdown():
    await close_database()

def do_stuff():
    return {"stuff": "done"}


@app.get("/healthcheck")
async def healthcheck():
    return "OK"

CORSMiddleware(
    app=app,
    allow_origins=[settings.website_domain],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)