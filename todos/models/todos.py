
from datetime import datetime
from sqlmodel import SQLModel,Field

class Todo(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str
    is_completed:bool

class UpdateTodo(SQLModel):
    title: str|None
    description: str|None
    is_completed:bool |None


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    phone: str
    address: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())       