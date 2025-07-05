from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
	text: str

class Todo(BaseModel):
	id: str
	text: str