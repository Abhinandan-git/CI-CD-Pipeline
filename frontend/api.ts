import { Todo } from "./types/tasks";

const baseUrl = 'http://127.0.0.1:8000';

export const getAllTodos = async (): Promise<Todo[]> => {
  const res = await fetch(`${baseUrl}/tasks`);
  const todos = await res.json();
  return todos;
}

export const addTodo = async (todo: Todo): Promise<Todo> => {
  const res = await fetch(`${baseUrl}/tasks`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(todo)
  })
  const newTodo = await res.json();
  return newTodo;
}

export const editTodo = async (todo: Todo): Promise<Todo> => {
  const res = await fetch(`${baseUrl}/tasks/${todo.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(todo)
  })
  const updatedTodo = await res.json();
  return updatedTodo;
}

export const deleteTodo = async (id: string): Promise<void> => {
  await fetch(`${baseUrl}/tasks/${id}`, {
    method: 'DELETE',
  })
}
