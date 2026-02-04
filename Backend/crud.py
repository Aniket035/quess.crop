from sqlalchemy.orm import Session
from models import Employee, Attendance   
from schemas import EmployeeCreate, AttendanceCreate

def create_employee(db: Session, employee: EmployeeCreate):
    if db.query(Employee).filter(Employee.employee_id == employee.employee_id).first():
        raise ValueError("Employee ID already exists")
    if db.query(Employee).filter(Employee.email == employee.email).first():
        raise ValueError("Email already exists")
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_employees(db: Session):
    return db.query(Employee).all()

def delete_employee(db: Session, employee_id: int):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False

def create_attendance(db: Session, attendance: AttendanceCreate, employee_id: int):
    db_attendance = Attendance(**attendance.dict(), employee_id=employee_id)
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def get_attendances(db: Session, employee_id: int):
    return db.query(Attendance).filter(Attendance.employee_id == employee_id).all()