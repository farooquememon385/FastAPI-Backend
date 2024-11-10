from fastapi import FastAPI, Depends, HTTPException
from database import init_db
from routes import *


app = FastAPI()

init_db()

@app.get("/")
async def index():
    return {"message": "Hello World"}

app.include_router(department_router)
app.include_router(course_router)
app.include_router(student_router)