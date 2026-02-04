from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .models import Employee as EmployeeModel
from database import SessionLocal, init_db
from schemas import EmployeeCreate, Employee, AttendanceCreate, Attendance
from crud import create_employee, get_employees, delete_employee, create_attendance, get_attendances

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173", "https://aniquesscorp.vercel.app/"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
init_db()  

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employees/", response_model=Employee)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return create_employee(db, employee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/employees/", response_model=list[Employee])
def list_employees(db: Session = Depends(get_db)):
    return get_employees(db)

@app.delete("/employees/{employee_id}")
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    if delete_employee(db, employee_id):
        return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees/{employee_id}/attendance/", response_model=Attendance)
def mark_attendance(employee_id: int, attendance: AttendanceCreate, db: Session = Depends(get_db)):
   
    if not db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first():
        raise HTTPException(status_code=404, detail="Employee not found")
    return create_attendance(db, attendance, employee_id)

@app.get("/employees/{employee_id}/attendance/", response_model=list[Attendance])
def view_attendance(employee_id: int, db: Session = Depends(get_db)):
    return get_attendances(db, employee_id)