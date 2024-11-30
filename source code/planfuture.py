import tkinter as tk
from tkinter import messagebox, simpledialog

class PlanYourFuturePage:
    def __init__(self, master):
        self.master = master
        self.master.title("Plan Your Future")
        self.master.geometry("600x600")

        
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)

        for i in range(600):
            color = f'#{max(0, min(i // 2, 255)):02x}4C{max(0, min(255 - i // 2, 255)):02x}'
            self.canvas.create_line(0, i, 600, i, fill=color)

        
        self.task_frame = tk.Frame(master, bg="white")
        self.task_frame.place(relx=0.5, rely=0.35, anchor="center")

        self.task_listbox = tk.Listbox(self.task_frame, width=60, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind("<Double-1>", self.modify_task_status)

       
        self.entry_frame = tk.Frame(master, bg="white")
        self.entry_frame.place(relx=0.5, rely=0.7, anchor="center")

        
        self.control_frame = tk.Frame(master, bg="white")
        self.control_frame.place(relx=0.5, rely=0.8, anchor="center")

       
        self.add_task_button = self.create_task_button("Add Task", self.add_task, "lightblue")
        self.delete_task_button = self.create_task_button("Delete Task", self.delete_task, "lightgreen")
        self.prepone_task_button = self.create_task_button("Prepone Task", self.prepone_task, "lightcoral")
        self.postpone_task_button = self.create_task_button("Postpone Task", self.postpone_task, "lightyellow")

        
        self.tasks = []  

    def create_task_button(self, text, command, color):
        """Creates a task management button with a specified color."""
        button = tk.Button(
            self.control_frame,
            text=text,
            command=command,
            bg=color,
            fg="black",
            font=("Arial", 12),
            relief="flat",
            padx=10,
            pady=5
        )
        button.pack(side="left", padx=10) 
        button.bind("<Enter>", lambda event, b=button: b.config(bg="blue", fg="white"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg=color, fg="black"))
        return button

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            deadline = simpledialog.askstring("Add Deadline", "Enter the deadline (e.g., YYYY-MM-DD):")
            if deadline:
                new_task = {"task": task, "status": "Incomplete", "deadline": deadline}
                self.tasks.append(new_task)
                self.update_task_listbox()
                messagebox.showinfo("Add Task", f"Task '{task}' added with deadline '{deadline}'.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_to_delete = self.tasks[selected_index[0]]
            task_name = task_to_delete["task"]
            self.tasks.pop(selected_index[0])
            self.update_task_listbox()
            messagebox.showinfo("Delete Task", f"Task '{task_name}' deleted.")
        else:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

    def prepone_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index and selected_index[0] > 0:
            self.tasks.insert(selected_index[0] - 1, self.tasks.pop(selected_index[0]))
            self.update_task_listbox()
            self.task_listbox.selection_set(selected_index[0] - 1)

    def postpone_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index and selected_index[0] < len(self.tasks) - 1:
            self.tasks.insert(selected_index[0] + 1, self.tasks.pop(selected_index[0]))
            self.update_task_listbox()
            self.task_listbox.selection_set(selected_index[0] + 1)

    def modify_task_status(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_status = simpledialog.askstring("Modify Status", "Enter new status (Completed, In Progress, Incomplete):")
            if new_status in ["Completed", "In Progress", "Incomplete"]:
                task_name = task["task"]
                task["status"] = new_status
                self.update_task_listbox()
                messagebox.showinfo("Modify Status", f"Task '{task_name}' status updated to '{new_status}'.")
            else:
                messagebox.showwarning("Invalid Status", "Please enter a valid status.")

    def update_task_listbox(self):
        
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['status']} (Deadline: {task['deadline']})")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlanYourFuturePage(root)
    root.mainloop()
