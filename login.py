import tkinter as tk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3
import register
import subprocess


def create_login_frame(master):
    for widget in master.winfo_children():
        widget.destroy()

    original_image = Image.open("birb.jpeg")  
    resized_image = original_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)

    bg_label = tk.Label(master, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    title_label = tk.Label(
        master, text="Heart Disease Detection using SVM",
        font=("Times New Roman", 24, "bold"), bg='#44badf', fg='black', pady=10
    )
    title_label.place(x=0, y=0, width=master.winfo_screenwidth())

    login_label = tk.Label(master, text="Admin Login", font=("Times New Roman", 18, "bold"), bg='#12beff', fg='black')
    login_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER, width=350, height=50)

    auth_frame = tk.Frame(master, bg='white')
    auth_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=350, height=300)

    tk.Label(auth_frame, text="Username:", font=("Times New Roman", 14), bg='white').grid(row=0, column=0, padx=20, pady=20)
    username = tk.StringVar()
    tk.Entry(auth_frame, textvariable=username, font=("Times New Roman", 14), relief='solid').grid(row=0, column=1, padx=20, pady=20)

    tk.Label(auth_frame, text="Password:", font=("Times New Roman", 14), bg='white').grid(row=1, column=0, padx=20, pady=20)
    password = tk.StringVar()
    tk.Entry(auth_frame, textvariable=password, font=("Times New Roman", 14), relief='solid', show="*").grid(row=1, column=1, padx=20, pady=20)

    tk.Button(
        auth_frame, text="Login", command=lambda: login(username, password, master),
        font=("Times New Roman", 18), fg="Black", bg='#2be040', relief='raised'
    ).grid(row=2, column=0, columnspan=2, pady=30)

    register_label = tk.Label(
        auth_frame, text="Don't have an account? Register", font=("Times New Roman", 10),
        fg="blue", bg="white", cursor="hand2"
    )
    register_label.grid(row=4, column=0, columnspan=2)
    register_label.bind("<Button-1>", lambda e: show_registration_frame(master))


def login(username, password, master):
    """Handle user login."""
    if not username.get() or not password.get():
        ms.showerror("Error", "Username and Password cannot be empty.")
        return

    try:
        with sqlite3.connect('users.db') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username.get(), password.get()))
            if cursor.fetchone():
                ms.showinfo("Login Successful", "Welcome! You have successfully logged in.")
                master.destroy()  
                import master
                master.Data_Preprocessing()
            else:
                ms.showerror("Error", "Invalid Username or Password.")
    except sqlite3.Error as e:
        ms.showerror("Database Error", f"Error accessing the database: {e}")


def show_registration_frame(master):
    """Display the registration frame."""
    register.show_registration_frame(master)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    create_login_frame(root)
    root.state('zoomed')
    root.mainloop()
