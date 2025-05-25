from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:4200",
]
app = FastAPI()

fake_todo_list_data = [{"todoName":"do homework", "description":"in 30 mins", "status":False}, {"todoName":"do homework1", "description":"in 30 mins", "status":False}, {"todoName":"do homework2", "description":"in 30 mins", "status":False}, {"todoName":"do homework6", "description":"in 30 mins", "status":False}, {"todoName":"do homework4", "description":"in 30 mins", "status":False}]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    # Return whatever you want, it will automaticly convert to json
    return fake_todo_list_data