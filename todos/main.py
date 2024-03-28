from fastapi import FastAPI
import uvicorn

app=FastAPI()

students:list=[{
    "name":"khizar",
    "rollno":30,
    "age":21,
    "section":"A",
}]
@app.get("/")
def helloWorld():
    return {"hello": "world"}
# this line will call this function automatically when the server starts.

@app.get("/students")
def get_students():
    return students


@app.get("/singlestudent")
async def get_student_by_query(rollno: int): 
    for student in students:
        if rollno is not None and student.get("rollno") == rollno:
            return student

    return {"message": "Student not found"}

@app.post("/students")
def add_student(name:str,rollno:int,age:int,section:str):
    students.append({"name":name,"rollno":rollno,"age":age,"section":section})
    return students
   


@app.put("/students/{student_id}")
def update_student(student_id: int, name: str , rollno: int, age: int, section: str):
    

    student_found = False
    for i, student in enumerate(students):
        if student.get("rollno") == student_id:
            student_found = True
            if name is not None:
                student["name"] = name
            if rollno is not None:
                student["rollno"] = rollno
            if age is not None:
                student["age"] = age
            if section is not None:
                student["section"] = section


            break

    if student_found:
        return student
    else:
        return {"message": f"Student with roll number {student_id} not found."}



@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
   

    print(f"Deleting student with roll number: {student_id}")  # Debugging print

    student_found = False
    for i, student in enumerate(students):
        if student.get("rollno") == student_id:
            print(f"Found student at index: {i}")  
            del students[i]
            student_found = True
            break

    if student_found:
        return {"message": f"Student with roll number {student_id} deleted successfully."}
    else:
        return {"message": f"Student with roll number {student_id} not found."}




def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


