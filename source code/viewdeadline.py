import tkinter as tk
from tkinter import messagebox, simpledialog


class DeadlineManagerPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Deadline Manager")
        self.master.geometry("600x600")  # Fixed window size
        self.master.resizable(False, False)  # Disable resizing

        # Gradient background
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient()

        # Task list display (entry field)
        self.task_frame = tk.Frame(self.canvas, bg="white")
        self.task_frame.place(relx=0.5, rely=0.35, anchor="center")  # Adjust vertical position

        self.task_listbox = tk.Listbox(self.task_frame, width=60, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10, fill="both", expand=True)
        self.task_listbox.bind("<Double-1>", self.toggle_task_status)  # Bind double-click to toggle status

        # Frame for buttons below the task list
        self.control_frame = tk.Frame(self.canvas, bg="white")
        self.control_frame.place(relx=0.5, rely=0.75, anchor="center")  # Place below the task list

        # Create buttons
        self.create_button("Add Task", self.add_task, "lightblue")
        self.create_button("Modify Deadlines", self.modify_deadline, "lightgreen")
        self.create_button("Delete Completed Tasks", self.delete_completed_tasks, "lightpink")
        self.create_button("Reset All Deadlines", self.reset_deadlines, "lightgray")

        # Tasks list
        self.tasks = [
            {"task": "Finish project", "deadline": "2024-12-10", "status": "Incomplete"},
            {"task": "Prepare for meeting", "deadline": "2024-12-05", "status": "Completed"},
        ]
        self.update_task_listbox()

    def draw_gradient(self):
        """Draws a gradient background on the canvas."""
        for i in range(600):
            color = f'#{max(0, min(i // 2, 255)):02x}4C{max(0, min(255 - i // 2, 255)):02x}'
            self.canvas.create_line(0, i, 600, i, fill=color)

    def create_button(self, text, command, color):
        """Creates a button with hover effect."""
        button = tk.Button(
            self.control_frame,
            text=text,
            command=command,
            bg=color,
            fg="black",
            font=("Arial", 12),
            relief="flat",
            padx=10,
            pady=5,
            width=20
        )
        button.pack(side="top", pady=5)  # Stack buttons vertically with spacing

        # Hover effect
        button.bind("<Enter>", lambda event, b=button: b.config(bg="blue", fg="white"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg=color, fg="black"))

    def update_task_listbox(self):
        """Refresh the task list display."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['deadline']} ({task['status']})")

    def toggle_task_status(self, event):
        """Toggle the status of the selected task between 'Completed' and 'Incomplete'."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            # Toggle status
            task["status"] = "Completed" if task["status"] == "Incomplete" else "Incomplete"
            self.update_task_listbox()
            messagebox.showinfo("Task Status", f"Status for '{task['task']}' changed to {task['status']}.")
        else:
            messagebox.showwarning("Task Status", "Select a task to change its status.")

    def add_task(self):
        """Add a new task to the list."""
        new_task = simpledialog.askstring("Add Task", "Enter the task:")
        if new_task:
            deadline = simpledialog.askstring("Add Task", "Enter the deadline (YYYY-MM-DD):")
            status = "Incomplete"  # Default status for new tasks
            self.tasks.append({"task": new_task, "deadline": deadline or "No Deadline", "status": status})
            self.update_task_listbox()
            messagebox.showinfo("Add Task", f"Task '{new_task}' has been added.")

    def modify_deadline(self):
        """Modify the deadline for a selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_deadline = simpledialog.askstring("Modify Deadline", f"Enter new deadline for '{task['task']}' (YYYY-MM-DD):")
            if new_deadline:
                task["deadline"] = new_deadline
                self.update_task_listbox()
                messagebox.showinfo("Modify Deadline", f"Deadline for '{task['task']}' updated to {new_deadline}.")
        else:
            messagebox.showwarning("Modify Deadline", "Select a task to modify the deadline.")

    def delete_completed_tasks(self):
        """Delete all tasks marked as completed."""
        self.tasks = [task for task in self.tasks if task["status"] != "Completed"]
        self.update_task_listbox()
        messagebox.showinfo("Delete Completed Tasks", "All completed tasks have been deleted.")

    def reset_deadlines(self):
        """Reset deadlines for all tasks."""
        for task in self.tasks:
            task["deadline"] = "No Deadline"
        self.update_task_listbox()
        messagebox.showinfo("Reset Deadlines", "All deadlines have been reset.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlineManagerPage(root)
    root.mainloop()
