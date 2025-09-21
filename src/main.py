from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    name: str
    des: str

# in-memory database
todos: List[Todo] = []

@app.get("/")
def index():
    return {"Message": "hello world"}

@app.get("/todo")
def get_todos():
    return todos

@app.post("/todo")
def add_todo(todo: Todo):
    todos.append(todo)
    return todos

@app.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return todos
    return {"error": "Todo Not Found"}

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted = todos.pop(index)
            return {"message": "Todo deleted successfully", "todo": deleted}
    return {"error": "Todo Not Found"}
