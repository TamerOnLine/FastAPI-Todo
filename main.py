 
import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from app.models.todo import Todo
from pydantic import BaseModel
from typing import Optional
from typing import List
from app.schemas.schemas import TodoResponse, TodoUpdate
from sqlalchemy.orm import Session



app = FastAPI(title="FastAPI",
              description="Hello Word",
              version="v01.0.0")


# Function 'get_db': Describe its purpose and usage here.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


@app.get("/")
# Function 'read_root': Describe its purpose and usage here.
def read_root():
    return {"Message": "Hello, FastAPI"}


@app.post("/todos/")
# Function 'create_todo': Describe its purpose and usage here.
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return {"message": " S  ", "todo": new_todo}

@app.get("/items/{item_id}")
# Function 'read_item': Describe its purpose and usage here.
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/todos/", response_model=List[TodoResponse])
# Function 'list_todos': Describe its purpose and usage here.
def list_todos(db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return todos


@app.delete("/todos/{item_id}")
# Function 'delete_todo': Describe its purpose and usage here.
def delete_todo(item_id: int, db: Session = Depends(get_db)):

    todo_item = db.query(Todo).filter(Todo.id == item_id).first()
    

    if todo_item is None:
        raise HTTPException(status_code=404, detail="No")
    

    db.delete(todo_item)
    db.commit()
    return {"message": "Item deleted successfully"}


@app.put("/todos/{item_id}", response_model=TodoResponse)
# Function 'update_todo': Describe its purpose and usage here.
def update_todo(item_id: int, todo: TodoUpdate, db: Session = Depends(get_db)):
    todo_item = db.query(Todo).filter(Todo.id == item_id).first()
    
    if todo_item is None:
        raise HTTPException(status_code=404, detail=f"Todo item with id {item_id} not found.")
    
    if todo.title is not None:
        setattr(todo_item, "title", todo.title)

    if todo.description is not None:
        setattr(todo_item, "description", todo.description)

    if todo.completed is not None:
        setattr(todo_item, "completed", todo.completed) 

    db.commit()
    db.refresh(todo_item)
    return todo_item


