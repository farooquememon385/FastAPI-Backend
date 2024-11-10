from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.CourseTaught import Department
from schemas import DepartmentCreate, DepartmentResponse
from app.crud.crud import create_department, get_department, update_department, delete_department, get_all_departments
from app.database.database import SessionLocal  # Ensure this function is available for database sessions

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Department Endpoints ---
# @app.post("/departments/", response_model=Department)
# def create_department_endpoint(department: DepartmentCreate, db: Session = Depends(get_db)):
#     return create_department(db, department)

# @app.get("/departments/{department_id}", response_model=Department)
# def get_department_endpoint(department_id: int, db: Session = Depends(get_db)):
#     db_department = get_department(db, department_id)
#     if db_department is None:
#         raise HTTPException(status_code=404, detail="Department not found")
#     return db_department

# @app.put("/departments/{department_id}", response_model=Department)
# def update_department_endpoint(department_id: int, department: DepartmentCreate, db: Session = Depends(get_db)):
#     db_department = update_department(db, department_id, department)
#     if db_department is None:
#         raise HTTPException(status_code=404, detail="Department not found")
#     return db_department

# @app.delete("/departments/{department_id}", response_model=Department)
# def delete_department_endpoint(department_id: int, db: Session = Depends(get_db)):
#     db_department = delete_department(db, department_id)
#     if db_department is None:
#         raise HTTPException(status_code=404, detail="Department not found")
#     return db_department

@app.get("/departments/", response_model=list[Department])
def get_all_departments_endpoint(db: Session = Depends(get_db)):
    return get_all_departments(db)