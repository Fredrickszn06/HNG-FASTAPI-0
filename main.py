from fastapi import FastAPI, status 
from datetime import datetime,timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",status_code=status.HTTP_200_OK)
async def get_info():
    return {
        "email": "obiekwufredrick519@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), 
        "github_url": "https://github.com/Fredrickszn06/HNG-FASTAPI-0",
    }
