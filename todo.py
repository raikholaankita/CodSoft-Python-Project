import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, bg="green", fg="white")
add_btn.pack(side=tk.LEFT, padx=5)

del_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task, bg="red", fg="white")
del_btn.pack(side=tk.LEFT, padx=5)

# Listbox for tasks
listbox = tk.Listbox(root, font=("Arial", 12))
listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()