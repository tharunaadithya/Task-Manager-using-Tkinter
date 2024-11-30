import tkinter as tk
from tkinter import messagebox
import random


class TaskManagerPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager - Sort & Shuffle")
        self.master.geometry("600x600")  # Fixed window size
        self.master.resizable(False, False)  # Disable resizing

        
        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.draw_gradient()

        
        self.task_frame = tk.Frame(self.canvas, bg="white")
        self.task_frame.place(relx=0.5, rely=0.35, anchor="center")  # Adjust vertical position

        self.task_listbox = tk.Listbox(self.task_frame, width=60, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10, fill="both", expand=True)

        
        self.control_frame = tk.Frame(self.canvas, bg="white")
        self.control_frame.place(relx=0.5, rely=0.75, anchor="center")  # Place below the task list

        
        self.create_button("Sort Tasks by Deadline", self.sort_tasks_by_deadline, "lightgreen")
        self.create_button("Shuffle Tasks", self.shuffle_tasks, "lightblue")
        self.create_button("Reset Task Order", self.reset_task_order, "lightcoral")  # Essential button
        self.create_button("Close Application", self.close_application, "lightgray")

        
        self.tasks = [
            {"task": "Finish project", "deadline": "2024-12-10"},
            {"task": "Prepare for meeting", "deadline": "2024-12-05"},
            {"task": "Buy groceries", "deadline": "2024-12-07"},
            {"task": "Call the bank", "deadline": "2024-12-08"},
        ]
        self.original_order = self.tasks[:]  # Backup of the original order
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
            self.task_listbox.insert(tk.END, f"{task['task']} - {task['deadline']}")

    def sort_tasks_by_deadline(self):
        """Sort tasks based on their deadlines."""
        self.tasks.sort(key=lambda x: x["deadline"])
        self.update_task_listbox()
        messagebox.showinfo("Sort Tasks", "Tasks have been sorted by deadline.")

    def shuffle_tasks(self):
        """Shuffle the order of tasks randomly."""
        random.shuffle(self.tasks)
        self.update_task_listbox()
        messagebox.showinfo("Shuffle Tasks", "Tasks have been shuffled.")

    def reset_task_order(self):
        """Reset tasks to their original order."""
        self.tasks = self.original_order[:]
        self.update_task_listbox()
        messagebox.showinfo("Reset Task Order", "Task order has been reset to the original order.")

    def close_application(self):
        """Close the application."""
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerPage(root)
    root.mainloop()
