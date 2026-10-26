
from fastapi import FastAPI
app = FastAPI()
# Temporary data storage
students = {
    1: {"name": "Ravi", "age": 21},
    2: {"name": "Priya", "age": 22}
}

# GET - Retrieve all students
@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/students")
def get_students():
    return students


# POST - Create a new student
@app.post("/students")
def create_student(student: dict):
    new_id = max(students.keys(), default=0) + 1
    students[new_id] = student
    return {
        "id": new_id,
        "student": student
    }


# PUT - Update an existing student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: dict):
    if student_id not in students:
        return {"error": "Student not found"}

    students[student_id] = student

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


# DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "Student not found"}

    del students[student_id]

    return {"message": "Student deleted successfully"}
