import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task != "":
        tasks.append(task)
        update_task_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        del tasks[selected_task_index]
        update_task_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = entry_task.get()
        if new_task != "":
            tasks[selected_task_index] = new_task
            update_task_listbox()
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

def update_task_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

def main():
    global root, entry_task, task_listbox

    root = tk.Tk()
    root.title("To-Do List App")
    root.config(bg="#ffefd5")

    frame = tk.Frame(root, bg="#ffefd5")
    frame.pack(pady=10)

    task_listbox = tk.Listbox(
        frame,
        width=50,
        height=10,
        selectmode=tk.SINGLE,
        font=("Helvetica", 12),
        bg="#fff8dc",
        fg="#8b4513",
        selectbackground="#cd5c5c"
    )
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

    task_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)

    entry_task = tk.Entry(
        root,
        width=50,
        font=("Helvetica", 12),
        bg="#fafad2",
        fg="#8b4513",
        insertbackground="#8b4513"
    )
    entry_task.pack(pady=10)

    add_task_button = tk.Button(
        root,
        text="Add Task",
        width=48,
        command=add_task,
        bg="#32cd32",
        fg="#ffffff",
        activebackground="#228b22"
    )
    add_task_button.pack(pady=5)

    update_task_button = tk.Button(
        root,
        text="Update Task",
        width=48,
        command=update_task,
        bg="#ffa500",
        fg="#ffffff",
        activebackground="#ff8c00"
    )
    update_task_button.pack(pady=5)

    delete_task_button = tk.Button(
        root,
        text="Delete Task",
        width=48,
        command=delete_task,
        bg="#dc143c",
        fg="#ffffff",
        activebackground="#b22222"
    )
    delete_task_button.pack(pady=5)

    creator_label = tk.Label(
        root,
        text="Created by Vedanta Dutta",
        font=("Helvetica", 10),
        bg="#ffefd5",
        fg="#8b4513"
    )
    creator_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
