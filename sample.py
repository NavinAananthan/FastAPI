from fastapi import FastAPI

app=FastAPI()


# Sample students data
students={
    1:{
        "name":"navin",
        "age":"20",
        "year":"3rd"
    }
}


# This is for the get request
@app.get("/")
def index():
    return {"Hello": "world"}

# This is to get the details of the students when id is given
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]