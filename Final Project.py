# To-Do list Manager


import tkinter as tk
from tkinter import messagebox, simpledialog


app = tk.Tk()
app.title("To-Do List Manager")
app.geometry("400x400")


# Function to Add a task
def add_task():
    title = entry_task.get()
    priority = entry_priority.get()
    due_date = entry_due_date.get()
    
    if title:
        task_listbox.insert(tk.END, f"{title} (Priority: {priority}, Due Date: {due_date})")
        entry_task.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task title.")

# Function to Remove a task
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to Edit a task
def edit_task():
    try:
        selected_task = task_listbox.curselection()[0]
        current_task = task_listbox.get(selected_task)
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=current_task)
        if new_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Buttons and Labels
label_task = tk.Label(app, text="Enter a Task:") #Task Label
entry_task = tk.Entry(app, width=40) #Task Entry Box
label_priority = tk.Label(app, text="Priority:") #Priority Label
entry_priority = tk.Entry(app, width=15) #Priority Entry Box
label_due_date = tk.Label(app, text="Due Date:") #Due Date label
entry_due_date = tk.Entry(app, width=40) #Due Date Entry Box
add_button = tk.Button(app, text="Add Task", width=40, command=add_task) #Button to Add task
remove_button = tk.Button(app, text="Remove Task", width=40, command=remove_task) #Button to Remove task
edit_button = tk.Button(app, text="Edit Task", width=40, command=edit_task) #Button to Edit task
task_listbox = tk.Listbox(app, selectbackground="yellow", height=10, width=55) #Task List BoxSS

# pack
label_task.pack()
entry_task.pack()
label_priority.pack()
entry_priority.pack()
label_due_date.pack()
entry_due_date.pack()
add_button.pack()
remove_button.pack()
edit_button.pack()
task_listbox.pack()

app.mainloop()
