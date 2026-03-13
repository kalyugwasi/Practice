from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI,Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
DATABASE_URL = "postgresql://postgres:password@localhost:5432/studentdb"

app = FastAPI()
students = {
    1:{
        "name":"john",
        "age":17,
        "year" :"year 12"
    }
}

class Student(BaseModel):
    name :str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
    
@app.get("/")
def index():
    return {"name":"First Date"}

@app.get("/get-student/{student_id}")  
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    if student_id in students:
        return students[student_id]
    return {"response":"land pakad le"}

@app.get("/get-by-name/{students_id}")
def get_student(*,student_id: int, name:Optional[str] = None,test:int):
    for std in students:
        if students[std]["name"] == name:
            return students[std]
    return {"Data": "Not Found"}


@app.post("/create-student/{students_id}")
def create_student(student_id: int,student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error":"student doesn not exist"}
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
        
    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"error":"student doesn not exist"}
    del students[student_id]
    return {"message":"student deleted successfully"}

