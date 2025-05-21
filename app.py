import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to delete a selected task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_list()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Function to rename a selected task
def rename_task():
    selected_task = task_listbox.curselection()
    new_name = rename_entry.get()
    if selected_task and new_name:
        tasks[selected_task[0]] = new_name
        update_list()
        rename_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Select a task and enter a new name!")

# Function to update the task list display
def update_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# UI Elements
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

# Rename section
rename_entry = tk.Entry(root, width=40)
rename_entry.pack(pady=10)

rename_button = tk.Button(root, text="Rename Task", command=rename_task)
rename_button.pack()

root.mainloop()
