from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"course": "IEE 305", "assignment": "HW9"}

@app.get("/student/{name}")
def get_student(name: str):
    return {"message": f"Hello {name}!"}