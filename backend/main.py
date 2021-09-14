from fastapi import FastAPI

# CORS: Cross Origin [protocol, domain, port] Resource Sharing [like in Django]
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Establishes connection with FastAPI and React

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES

@app.get("/")
def read_root():
    return {"Wu":"Tang"}

@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1

@app.post("/api/todo")
async def post_todo(todo):
    return 1

@app.put("/api/todo{id}")
async def put_todo(id, data):
    return 1

@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1

"""
>> uvicorn main:app --reload
changes reflect instantly on webpage

launch page/docs reveals all routes and params
"""