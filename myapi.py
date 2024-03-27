from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name": "rahaji",
        "age": 20,
        "major": "informatics"
    }
}

class Student(BaseModel):
    name: str
    age: int
    major: str

class updateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    major: Optional[str] = None

@app.get("/")
def index():
    return {"name":"first data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of student you want to view", gt=0)):
    return students[student_id]

@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error":"student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:updateStudent):
    if student_id not in students:
        return {"error":"student does not exists"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.major != None:
        students[student_id].major = student.major
    
    return students[student_id]
    
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error":"student does not exists"}
    del students[student_id]
    return {"message":"student delete successfully"}