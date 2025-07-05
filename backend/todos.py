from fastapi import APIRouter
from bson.objectid import ObjectId
import database
from models import Todo

router = APIRouter(prefix="/tasks")

@router.get("/")
async def get_all_todos():
	collection = database.get_database()["todos"]
	documents = collection.find({})
	todos = []
	for document in documents:
		todos.append({
			"id": str(document["_id"]),
			"text": document["text"]
		})
	return todos

@router.post("/")
async def add_todo(text: Todo):
	collection = database.get_database()["todos"]
	todo_dict = text.model_dump(exclude={"id"})
	result = collection.insert_one(todo_dict)
	return {
		"id": str(result.inserted_id),
		"text": todo_dict["text"]
	}

@router.put("/{id}")
async def edit_todo(id: str, text: Todo):
	collection = database.get_database()["todos"]
	result = collection.find_one_and_update(
		{"_id": ObjectId(id)},
		{"$set": text.model_dump(exclude={"id"})},
		return_document=True
	)
	return {"_id": str(result["_id"]), "text": result["text"]}

@router.delete("/{id}")
async def delete_todo(id: str):
	collection = database.get_database()["todos"]
	collection.delete_one({"_id": ObjectId(id)})
