import tkinter as tk
from tkinter import messagebox, simpledialog

class WelcomePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome Page")
        self.master.geometry("500x500")

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        for i in range(500):
            color = f'#{i // 2:02x}4C{255 - i // 2:02x}'  
            self.canvas.create_line(0, i, 500, i, fill=color)

        self.frame = tk.Frame(master, bg='white', bd=5)
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=('Arial', 12))
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind('<Button-3>', self.show_context_menu)  # Right-click event

        self.button_view_tasks = tk.Button(self.frame, text="View Upcoming Tasks", command=self.view_tasks, bg='lightblue', font=('Arial', 12), width=25)
        self.button_view_tasks.pack(pady=10)

        self.button_add_task = tk.Button(self.frame, text="Add New Task", command=self.add_task, bg='lightgreen', font=('Arial', 12), width=25)
        self.button_add_task.pack(pady=10)

        self.button_delete_task = tk.Button(self.frame, text="Delete Task", command=self.delete_task, bg='salmon', font=('Arial', 12), width=25)
        self.button_delete_task.pack(pady=10)

        self.button_free_time = tk.Button(self.frame, text="Free Time", command=self.free_time, bg='lightyellow', font=('Arial', 12), width=25)
        self.button_free_time.pack(pady=10)

        self.tasks = []  # List of dictionaries: [{'task': str, 'status': str}, ...]

        # Context menu
        self.context_menu = tk.Menu(self.master, tearoff=0)
        self.context_menu.add_command(label="Prepone Task", command=self.prepone_task)
        self.context_menu.add_command(label="Postpone Task", command=self.postpone_task)
        self.context_menu.add_command(label="Mark as Completed", command=self.mark_as_completed)

    def view_tasks(self):
        if not self.tasks:
            messagebox.showinfo("View Tasks", "No upcoming tasks.")
        else:
            task_list = "\n".join(
                [f"{idx + 1}. {task['task']} - {task['status']}" for idx, task in enumerate(self.tasks)]
            )
            messagebox.showinfo("View Tasks", f"Upcoming Tasks:\n{task_list}")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            self.tasks.append({'task': task, 'status': 'Incomplete'})
            self.update_task_listbox()
            messagebox.showinfo("Add Task", f"Task '{task}' added.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_to_delete = self.tasks[selected_task_index[0]]['task']
            del self.tasks[selected_task_index[0]]
            self.update_task_listbox()
            messagebox.showinfo("Delete Task", f"Task '{task_to_delete}' deleted.")
        else:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['status']}")

    def free_time(self):
        messagebox.showinfo("Free Time", "You can manage your free time here.")

    def show_context_menu(self, event):
        try:
            self.selected_task_index = self.task_listbox.nearest(event.y)  
            self.task_listbox.selection_clear(0, tk.END)
            self.task_listbox.selection_set(self.selected_task_index)
            self.context_menu.post(event.x_root, event.y_root)
        except IndexError:
            pass  

    def prepone_task(self):
        if self.selected_task_index > 0:  
            self.tasks.insert(self.selected_task_index - 1, self.tasks.pop(self.selected_task_index))
            self.update_task_listbox()
            self.task_listbox.selection_set(self.selected_task_index - 1)

    def postpone_task(self):
        if self.selected_task_index < len(self.tasks) - 1:  
            self.tasks.insert(self.selected_task_index + 1, self.tasks.pop(self.selected_task_index))
            self.update_task_listbox()
            self.task_listbox.selection_set(self.selected_task_index + 1)

    def mark_as_completed(self):
        if hasattr(self, 'selected_task_index') and 0 <= self.selected_task_index < len(self.tasks):
            self.tasks[self.selected_task_index]['status'] = 'Completed'
            self.update_task_listbox()
            messagebox.showinfo("Task Update", "You did a good job completing the task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomePage(root)
    root.mainloop()
