from tkinter import*
from tkinter import messagebox
root = Tk()
root.title("To-Do List Application")
root.geometry("400x500")
root.resizable(False, False)

tasks_list = []

def add_task():
    task = task_entry.get()
    if task!= "":
        tasks_list.append(task)
        listbox_tasks.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showinfo("Warning", "Please enter task!") 
def delete_task():
            try:
                selected_index = listbox_tasks.curselection()[0]
                listbox_tasks.delete(selected_index)
                tasks_list.pop(selected_index)
            except:
                messagebox.showinfo("Warning","please select a task to delete")
def clear_task():
 
                    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks"):
                        listbox_tasks.delete(0, Tk.END)
                        tasks_list.clear()
heading=Label(root,text="To-Do List and Reminders", font = ("Arial", 16, "bold"))
heading.pack(pady=10)
task_entry=Entry(root, font = ("Arial", 12))
task_entry.pack(pady=10)
button1 = Button(root, text = "add task", width = 10, command = add_task, bg = "green", fg = "white")
button1.pack(pady=10)
button2 = Button(root, text = "Delete task", width = 10, command = delete_task, bg="red", fg = "white")
button2.pack(pady=10)
button3 =Button(root, text = "Clear task", width = 10, command = clear_task, bg="yellow", fg = "white")
button3.pack(pady=10)
listbox_frame =Frame(root)
listbox_frame.pack(pady=10)
listbox_tasks =Listbox(listbox_frame, width = 40, height=15, font = (12))
listbox_tasks.pack(side=LEFT,fill=BOTH)
count_label = Label(root, text = "Total Tasks: 0", font = (10))
count_label.pack(pady=5)
def update_count(*args):
    count_label.config(text=f"Total Tasks: {listbox_tasks.size()}")

listbox_tasks.bind("<<ListboxSelect>>", update_count)

root.mainloop()
