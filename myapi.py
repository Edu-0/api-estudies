from fastapi import FastAPI, Path # This object of FastAPI will be used later to create our APIs
from typing import Optional # It's just a good practice to add on Query Parameters, that way the endpoint stays valid even without a parameter

app = FastAPI() # The FastAPI object has many attributes and will be used

students = { # Just generated some with AI to test with
    1: {"name": "Eduardo", "age": 19, "grade": 12, "email": "eduardo@email.com"},
    2: {"name": "Mariana", "age": 18, "grade": 12, "email": "mariana@email.com"},
    3: {"name": "Lucas", "age": 17, "grade": 11, "email": "lucas@email.com"},
    4: {"name": "Ana", "age": 18, "grade": 12, "email": "ana@email.com"},
    5: {"name": "Rafael", "age": 16, "grade": 10, "email": "rafael@email.com"},
    6: {"name": "Beatriz", "age": 17, "grade": 11, "email": "beatriz@email.com"},
    7: {"name": "Gabriel", "age": 18, "grade": 12, "email": "gabriel@email.com"},
    8: {"name": "Camila", "age": 15, "grade": 9, "email": "camila@email.com"},
    9: {"name": "Thiago", "age": 16, "grade": 10, "email": "thiago@email.com"},
    10: {"name": "Isabela", "age": 17, "grade": 11, "email": "isabela@email.com"},
    11: {"name": "Eduardo", "age": 15, "grade": 5, "email": "eduardo2@email.com"}
}

@app.get("/") # Homepage
def index():
    return {
        "name": "First Data"
    } # FastAPI uses JSON

"""
Default get with id:

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]]
"""

@app.get("/students")
def get_students():
    return students

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(gt=0, description="ID of the student you want to view")):
    return students[student_id]
# The Path will serve to tell more about the parameter, enforce rules, add documentation, examples, make it required, etc...
# If a restriction is broken, like putting "get-student/-1", an error will be returned

@app.get("/get-by-name") # I want to get the "get-by-name?name=eduardo"
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Having more than one parameter:
@app.get("/get-by-age")
def get_student(*, name: Optional[str] = None, age: int): # We can't have a required parameter after an optional one, to bypass this restriction we add an * in the beginning, or just rearrange the parameters
    for student_id in students:
        if students[student_id]["age"] == age:
            return students[student_id]
    return {"Data": "Not found"}

# Mixing Path and Query Parameters:
@app.get("/get-by-name/{name}")
def get_student(*, student_id: Optional[int] = None, name: str): # If only the name is passed, it'll get the first occurrence, if a name + existing ID is passed, it'll search for the specific register
    name = name.lower()
    for std_id in students:
        if (students[std_id]["name"].lower() == name) and (std_id == student_id):
            return students[std_id]
        elif students[std_id]["name"].lower() == name and student_id is None:
            return students[std_id]
    return {"Data": "Not Found"}