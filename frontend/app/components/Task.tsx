"use client"

import { Todo } from "@/types/tasks"
import React, { FormEventHandler, useState } from "react"
import { FiEdit, FiTrash2 } from "react-icons/fi"
import Modal from "./Modal"

interface TaskProp {
	task: Todo
}

const Task: React.FC<TaskProp> = ({ task }) => {
	const [modalOpenEdit, setModalOpenEdit] = useState<boolean>(false);
	const [modalOpenDelete, setModalOpenDelete] = useState<boolean>(false);

	const [textToEdit, setTextToEdit] = useState<string>(task.text);

	const handleSubmitEditTodo: FormEventHandler<HTMLFormElement> = async (e) => {
		e.preventDefault()
		setModalOpenEdit(false)
	}

	const handleDeleteTask = async (id: string) => {
		setModalOpenDelete(false)
	}
		
	return (
		<tr key={task.id}>
			<td className="w-full">{task.text}</td>
			<td  className="flex gap-4">
				<FiEdit onClick={() => setModalOpenEdit(true)} cursor="pointer" size={20} />

				<Modal modalOpen={modalOpenEdit} setModalOpen={setModalOpenEdit}>
					<form onSubmit={handleSubmitEditTodo}>
						<h3 className="font-bold text-lg">Edit task</h3>
						<div className="modal-action">
							<input value={textToEdit} onChange={e => setTextToEdit(e.target.value)} type="text" placeholder="Edit task" className="input input-ghost w-full" />
							<button type="submit" className="btn">Submit</button>
						</div>
					</form>
				</Modal>

				<FiTrash2 onClick={() => setModalOpenDelete(true)} cursor="pointer" className="text-red-500" size={20} />

				<Modal modalOpen={modalOpenDelete} setModalOpen={setModalOpenDelete}>
					<h3 className="text-lg">Are you sure you want to delete this task</h3>
					<div className="model-action">
						<button className="btn w-full mt-4" onClick={() => handleDeleteTask(task.id)}>Yes</button>
					</div>
				</Modal>
			</td>
		</tr>
	)
}

export default Task
