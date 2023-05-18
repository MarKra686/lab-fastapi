from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

@app.post("/students/")
def create_student(student: StudentCreateSchema):
    return {"status": "ok", "student": student}


@app.get("/student/{student_id}")
async def read_student(student_id):
    return {"student_id": student_id}
