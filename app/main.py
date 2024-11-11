from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from database import init_db
from routes import *
from schemas.PayLoad import insertPayLoad
from crud import parse_csv, insert_data


app = FastAPI(
    title="Learning Management System",
    description="A simple Learning Management System API",
    version="1.0.0",
    contact={
        "name": "Farooq Memon",
    },
)

init_db()

@app.get("/")
async def index():
    return {"message": "Welcome to the Learning Management System!"}

app.include_router(department_router)
app.include_router(course_router)
app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(enrolled_router)
app.include_router(courseTaught_router)

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    parsed_data = await parse_csv(file=file, db=db)
    return parsed_data

@app.post("/upload-payload")
async def upload_payload(payload: insertPayLoad, db: Session = Depends(get_db)):
  print(payload)
  return await insert_data(payload=payload, db=db)
