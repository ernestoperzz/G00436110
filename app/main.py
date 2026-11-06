from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, StudentDB
from app.schemas import StudentCreate, StudentRead

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}


@app.post("/api/students", response_model= StudentRead, status_code = status.HTTP_201_CREATED)
def add_student(new_student:StudentCreate, db:Session = Depends(get_db)):
    db_student = StudentDB(**new_student_model_dump());
    db.add(db_student)
    try: 
        db.commit()
        db.refresh(db_student)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code= status.HTTP_409_CONFLICT, detail = "A student with these details already exists")
    return db_student


@app.get("/api/students", response_model = list[StudentRead])
def get_students(db:Session = Depends(get_db)):
    statement = select (StudentDB).order_by(StudentDB.id)
    return
db.execute(statement).scalars().all()