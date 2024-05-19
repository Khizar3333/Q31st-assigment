from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
import uvicorn
from dotenv import load_dotenv
from .config.db import createtables,connection
from .models.todos import Todo,UpdateTodo, Users

load_dotenv()

app=FastAPI()



# this command check where SQLModel is use and then create that tables    





@app.get("/getTodo")
def get_Todo():
    # advantage of with :create session,close session,error handling otherwise we have to do all things seperately
    with Session(connection) as session:
        statement=select(Todo) 
        # statement=select(Todo).where(Todo.id==1) 
        result=session.exec(statement)
        data=result.all()  
        print(data)   
        return data

@app.get("/get_todo{todo_id}")
def get_todos_single(todo_id:int):
    with Session(connection) as session:
        statement = select(Todo).where(Todo.id == todo_id)
        results = session.exec(statement)
        data = results.all()
        print(data)
        return data    

@app.get("/getuser")
def get_user():
    with Session(connection) as session:
        statement = select(Users)
        results = session.exec(statement)
        data = results.all()
        return data


@app.post("/Createtodo")
def create_todos(todos:Todo):
    with Session(connection) as session:
        session.add(todos)
        session.commit()
        session.refresh(todos)
        return {"status":200,"message":"todo created successfully"}   
        
@app.post("/createuser")
def create_user(user:Users):
    with Session(connection) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"status":200,"message":"user created successfully"}

@app.put("/updatetodo/{id}")
def update_todos(id:int,todo:UpdateTodo):
    with Session(connection) as session:
        dbtodo=session.get(Todo,id)
        if not dbtodo:
            raise HTTPException(status_code=404,detail="todo not found")
        tododata=todo.model_dump(exclude_unset=True)
        dbtodo.sqlmodel_update(tododata)
        session.add(dbtodo)
        session.commit()
        session.refresh(dbtodo)
        return {"status":200,"message":"todo updated successfully"}

@app.delete("/deletetodo/{todoid}")
def delete_todo(todoid:int):
     with Session(connection) as session:
        dbtodo=session.get(Todo,todoid)
        if not dbtodo:
            raise HTTPException(status_code=404,detail="todo not found")
        session.delete(dbtodo)
       
        return {"status":200,"message":"todo deleted successfully"}

def start():
    createtables()
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)


