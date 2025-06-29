import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ...src.database import models, controller

# In-memory SQLite database
TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Setup DB schema
@pytest.fixture(scope="function")
def db_session():
	models.Base.metadata.create_all(bind=engine)  # Create tables
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()
		models.Base.metadata.drop_all(bind=engine)  # Clean up

def test_create_todo(db_session):
    todo = controller.create_todo(db_session, "Test ToDo", "Testing description")
    assert todo.id is not None
    assert todo.title == "Test ToDo"
    assert todo.description == "Testing description"
    assert todo.completed is False

def test_get_todo(db_session):
    created = controller.create_todo(db_session, "Fetch me")
    fetched = controller.get_todo(db_session, created.id)
    assert fetched is not None
    assert fetched.id == created.id

def test_get_all_todos(db_session):
    controller.create_todo(db_session, "First")
    controller.create_todo(db_session, "Second")
    todos = controller.get_all_todos(db_session)
    assert len(todos) == 2

def test_update_todo(db_session):
    todo = controller.create_todo(db_session, "Old Title", "Old Desc")
    updated = controller.update_todo(db_session, todo.id, title="New Title", completed=True)
    assert updated.title == "New Title"
    assert updated.completed is True

def test_delete_todo(db_session):
    todo = controller.create_todo(db_session, "Delete me")
    success = controller.delete_todo(db_session, todo.id)
    assert success is True
    assert controller.get_todo(db_session, todo.id) is None

def test_delete_nonexistent_todo(db_session):
    success = controller.delete_todo(db_session, 999)
    assert success is False
