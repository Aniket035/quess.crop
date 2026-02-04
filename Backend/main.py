# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Plain imports — no dots (.) — this fixes the "attempted relative import with no known parent package" error
from models import Employee as EmployeeModel
from database import SessionLocal, init_db
from schemas import EmployeeCreate, Employee, AttendanceCreate, Attendance
from crud import create_employee, get_employees, delete_employee, create_attendance, get_attendances

app = FastAPI(
    title="HRMS Lite API",
    description="Lightweight HR Management System - Employee & Attendance",
    version="1.0.0"
)

# CORS configuration — added your Vercel frontend domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",           # Vite dev server
        "http://localhost:3000",           # sometimes used
        "https://aniquesscorp.vercel.app", # your live frontend
        "*"                                # temporary wildcard for debugging (remove later for security)
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables on startup
init_db()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ──────────────────────────────────────────────
# Employee Endpoints
# ──────────────────────────────────────────────

@app.post("/employees/", response_model=Employee, status_code=201)
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee
    """
    try:
        return create_employee(db, employee)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/employees/", response_model=list[Employee])
def list_employees(db: Session = Depends(get_db)):
    """
    Get all employees
    """
    return get_employees(db)


@app.delete("/employees/{employee_id}", status_code=200)
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Delete an employee by ID
    """
    if delete_employee(db, employee_id):
        return {"detail": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")


# ──────────────────────────────────────────────
# Attendance Endpoints
# ──────────────────────────────────────────────

@app.post(
    "/employees/{employee_id}/attendance/",
    response_model=Attendance,
    status_code=201
)
def mark_attendance(
    employee_id: int,
    attendance: AttendanceCreate,
    db: Session = Depends(get_db)
):
    """
    Mark attendance (Present/Absent) for an employee on a specific date
    """
    # Check if employee exists
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return create_attendance(db, attendance, employee_id)


@app.get("/employees/{employee_id}/attendance/", response_model=list[Attendance])
def view_attendance(employee_id: int, db: Session = Depends(get_db)):
    """
    Get all attendance records for a specific employee
    """
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return get_attendances(db, employee_id)


# Optional: root endpoint for quick health check
@app.get("/")
def root():
    return {
        "message": "HRMS Lite API is running",
        "docs": "/docs",
        "redoc": "/redoc"
    }