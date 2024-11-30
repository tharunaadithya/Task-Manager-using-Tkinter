import tkinter as tk
from tkinter import messagebox
import subprocess


user_db = {"tharun": "1234", "admin": "7890"}


def on_login():
    username = entry_username.get()
    password = entry_password.get()
    if username in user_db and user_db[username] == password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
        root.destroy()
        subprocess.run(['python','menu.py'])
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        

def on_signup():
    username = entry_username.get()
    password = entry_password.get()
    if username in user_db:
        messagebox.showerror("Signup Failed", "Username already exists.")
    elif username == "" or password == "":
        messagebox.showerror("Signup Failed", "Username and password cannot be empty.")
    else:
        user_db[username] = password
        messagebox.showinfo("Signup Successful", f"Account created for {username}.")

        

def on_set_password():
    username = entry_username.get()
    if username not in user_db:
        messagebox.showerror("Set Password Failed", "Username does not exist.")
        return
    
    new_password = entry_password.get()
    if new_password == "":
        messagebox.showerror("Set Password Failed", "New password cannot be empty.")
        return
    
    user_db[username] = new_password
    messagebox.showinfo("Set Password Successful", "Password updated successfully.")
    
    new_password = entry_password.get()
    if new_password == "":
        messagebox.showerror("Set Password Failed", "New password cannot be empty.")
        return
    
    user_db[username] = new_password
    messagebox.showinfo("Set Password Successful", "Password updated successfully.")

def on_forgot_password():
    username = entry_username.get()
    if username not in user_db:
        messagebox.showerror("Forgot Password Failed", "Username does not exist.")
        return
    elif username in user_db:
        messagebox.showinfo("dont worry", f"your old password is {user_db[username]}.")
        

def on_create_account():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in user_db:
        messagebox.showinfo("Create Account", "You are already a user.")
    elif username == "":
        messagebox.showerror("Create Account Failed", "Username should not be empty.")
    else:
        user_db[username] = password
        messagebox.showinfo("Create Account Successful", f"Account created for {username}.")



root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")


canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()


for i in range(400):
    color = f'#{i//2:02x}4C{255-i//2:02x}'  
    canvas.create_line(0, i, 400, i, fill=color)

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')


label_username = tk.Label(frame, text="Username:", bg='white', font=('Arial', 12))
label_username.pack(pady=5)

entry_username = tk.Entry(frame, font=('Arial', 12))
entry_username.pack(pady=5)


label_password = tk.Label(frame, text="Password:", bg='white', font=('Arial', 12))
label_password.pack(pady=5)

entry_password = tk.Entry(frame, show='*', font=('Arial', 12))
entry_password.pack(pady=5)


button_login = tk.Button(frame, text="Login", command=on_login, bg='lightblue', font=('Arial', 12))
button_login.pack(pady=10)


button_signup = tk.Button(frame, text="Sign Up", command=on_signup, bg='lightgreen', font=('Arial', 12))
button_signup.pack(pady=5)


button_set_password = tk.Button(frame, text="Set Password", command=on_set_password, bg='lightyellow', font=('Arial', 12))
button_set_password.pack(pady=5)


button_forgot_password = tk.Button(frame, text="Forgot Password", command=on_forgot_password, bg='lightcoral', font=('Arial', 12))
button_forgot_password.pack(pady=5)


button_create_account = tk.Button(frame, text="Create New Account", command=on_create_account, bg='lightpink', font=('Arial', 12))
button_create_account.pack(pady=5)


root.mainloop()