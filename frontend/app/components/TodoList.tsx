import React from "react";
import Task from "./Task";
import { Todo } from "@/types/tasks";

interface TodoListProps {
	tasks: Todo[]
}

const TodoList: React.FC<TodoListProps> = ({ tasks }) => {
	return (
		<div className="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
			<table className="table">
				<thead>
					<tr>
						<th>Tasks</th>
						<th>Actions</th>
					</tr>
				</thead>
				<tbody>
					{Array.isArray(tasks) && tasks.map(task => <Task key={task.id} task={task} />)}
				</tbody>
			</table>
		</div>
	)
}

export default TodoList;
