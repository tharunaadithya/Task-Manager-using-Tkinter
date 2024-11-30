import tkinter as tk
from tkinter import messagebox
import subprocess

class TaskPlannerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Planner")
        self.master.geometry("500x500")

      
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack(fill="both", expand=True)

        for i in range(500):  
            color = f'#{i // 2:02x}4C{255 - i // 2:02x}'  
            self.canvas.create_line(0, i, 500, i, fill=color)

   
        self.create_menubar()

      
        self.center_frame = tk.Frame(master, bg="white")
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

      
        self.create_hover_button("Plan Today", self.plan_today)
        self.create_hover_button("Plan Future", self.plan_future)
        self.create_hover_button("Prioritize Tasks", self.prioritize_tasks)
        self.create_hover_button("View Deadlines", self.view_deadlines)

    def create_menubar(self):
        """Creates the menubar with dropdowns."""
        menubar = tk.Menu(self.master)

      
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Task", command=self.plan_today)
        file_menu.add_command(label="Open Task", command=self.plan_future)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Prioritize Tasks", command=self.prioritize_tasks)
        edit_menu.add_command(label="View Deadlines", command=self.view_deadlines)
        menubar.add_cascade(label="Edit", menu=edit_menu)

     
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

       
        self.master.config(menu=menubar)

    def create_hover_button(self, text, command):
        """Creates a button with hover effects."""
        button = tk.Button(self.center_frame,text=text, command=command,bg="lightblue",fg="black",font=("Arial", 12),relief="flat",
            padx=10,
            pady=5,
            width=20
        )
        button.pack(pady=10) 

        
        button.bind("<Enter>", lambda event, b=button: b.config(bg="blue", fg="white"))
        button.bind("<Leave>", lambda event, b=button: b.config(bg="lightblue", fg="black"))

    def plan_today(self):
        messagebox.showinfo("Plan Today", "Here you can plan tasks for today!")
        root.destroy()
        subprocess.run(['python','welcome.py'])

    def plan_future(self):
        messagebox.showinfo("Plan Future", "Here you can plan tasks for the future!")
        root.destroy()
        subprocess.run(['python','planfuture.py'])

    def prioritize_tasks(self):
        messagebox.showinfo("Prioritize Tasks", "Here you can reorder and prioritize your tasks!")
        root.destroy()
        subprocess.run(['python','sort.py'])

    def view_deadlines(self):
        messagebox.showinfo("View Deadlines", "Here you can view all upcoming deadlines!")
        root.destroy()
        subprocess.run(['python','viewdeadline.py'])

    def show_about(self):
        messagebox.showinfo("About", "Task Planner Application\nVersion 1.0")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskPlannerApp(root)
    root.mainloop()
