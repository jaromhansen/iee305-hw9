from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"course": "IEE 305", "assignment": "HW9"}

@app.get("/student/{name}")
def get_student(name: str):
    return {"message": f"Hello {name}!"}

@app.get("/course")
def get_course_info():
    return {"course": "IEE 305",
            "title": "Information Systems Engineering",
            "semester": "Fall 2025"}