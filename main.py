from fastapi import FastAPI, status, Response, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials, initialize_app

app = FastAPI()
from database import puzzle_collection
credential = credentials.Certificate("./lemodikrysset-admin-credentials.json")
initialize_app(credential)
def check_token(res: Response, creds: HTTPAuthorizationCredentials=Depends(HTTPBearer(auto_error=False))):
    decoded = auth.verify_id_token(creds.credentials)
    return decoded




@app.get("/ping")
async def ping(user = Depends(check_token)):
    print(user)
    return do_stuff()


@app.get("/puzzle")
async def ping(id:str, user = Depends(check_token)):
    print(id)
    
    coll = await puzzle_collection.find_one({"publicId": id})
    print(coll)
    ts = coll["created"].as_datetime()
    print(repr(ts))
    data = {
        "id": coll["publicId"],
        "created": [ts]
    }
    return data




def do_stuff():
    user = auth
    return "stuff done"