from sqlalchemy.orm import Session
from . import models

# Create a new ToDo
def create_todo(db: Session, title: str, description: str | None = None) -> models.ToDo:
	todo = models.ToDo(title=title, description=description)
	db.add(todo)
	db.commit()
	db.refresh(todo)
	return todo

# Read (get) a ToDo by ID
def get_todo(db: Session, todo_id: int) -> models.ToDo | None:
	return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()

# Read all ToDos
def get_all_todos(db: Session, skip: int = 0, limit: int = 10) -> list[models.ToDo]:
	return db.query(models.ToDo).offset(skip).limit(limit).all()

# Update a ToDo
def update_todo(db: Session, todo_id: int, title: str | None = None, description: str | None = None, completed: bool | None = None) -> models.ToDo | None:
	todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
	if not todo:
		return None

	if title is not None:
		todo.title = title
	if description is not None:
		todo.description = description
	if completed is not None:
		todo.completed = completed

	db.commit()
	db.refresh(todo)
	return todo

# Delete a ToDo
def delete_todo(db: Session, todo_id: int) -> bool:
	todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
	if not todo:
		return False

	db.delete(todo)
	db.commit()
	return True
