from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ToDo(Base):
	__tablename__ = "todos"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(256), nullable=False)
	description = Column(String(1024), nullable=True)
	completed = Column(Boolean, default=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now())

	def __repr__(self):
		return f"<ToDo(id={self.id}, title='{self.title}', completed={self.completed})>"
