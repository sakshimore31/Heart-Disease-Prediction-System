import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import re  
import login


def validate_inputs(full_name, address, email, gender, mobile, username, password):
    """Validate registration inputs."""
    if not full_name or not full_name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Full Name must contain only letters and spaces.")
        return False
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format.")
        return False
    if not gender:
        messagebox.showerror("Error", "Please select your gender.")
        return False
    if not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Mobile number must be a 10-digit number.")
        return False
    if not username:
        messagebox.showerror("Error", "Username cannot be empty.")
        return False
    if not password or len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long.")
        return False
    return True


def register_user(full_name, address, email, gender, mobile, username, password):
    """Handle user registration."""
    
    if not validate_inputs(full_name, address, email, gender, mobile, username, password):
        return

    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                address TEXT,
                email TEXT,
                gender TEXT,
                mobile TEXT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')

        cursor.execute('''
            INSERT INTO users (full_name, address, email, gender, mobile, username, password)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (full_name, address, email, gender, mobile, username, password))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Account created successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def show_registration_frame(master):
    
    for widget in master.winfo_children():
        widget.destroy()

    original_image = Image.open("birb.jpeg")
    resized_image = original_image.resize((master.winfo_screenwidth(), master.winfo_screenheight()))
    bg_image = ImageTk.PhotoImage(resized_image)

    bg_label = tk.Label(master, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    tk.Label(master, text="Heart Disease Detection using SVM", fg='black', bg="#ffdde1", font=('ROBOTO', 28), height=1, width=70).place(x=0, y=0)

    frame = tk.Frame(master, height=550, width=460, bg="#ddd6f3")
    frame.place(x=550, y=180)

    tk.Label(frame, text="Full Name:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=50)
    full_name_entry = tk.Entry(frame, border=3, width=35)
    full_name_entry.place(x=180, y=50, height=30)

    tk.Label(frame, text="Address:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=100)
    address_entry = tk.Entry(frame, border=3, width=35)
    address_entry.place(x=180, y=100, height=30)

    tk.Label(frame, text="Email:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=150)
    email_entry = tk.Entry(frame, border=3, width=35)
    email_entry.place(x=180, y=150, height=30)

    tk.Label(frame, text="Gender:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=200)
    gender_var = tk.StringVar()
    gender_var.set("Male") 
    tk.Radiobutton(frame, text="Male", font=("Times New Roman", 14), bg="#ddd6f3", value="Male", variable=gender_var).place(x=200, y=200)
    tk.Radiobutton(frame, text="Female", font=("Times New Roman", 14), bg="#ddd6f3", value="Female", variable=gender_var).place(x=320, y=200)

    tk.Label(frame, text="Mobile No:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=250)
    mobile_entry = tk.Entry(frame, border=3, width=35)
    mobile_entry.place(x=180, y=250, height=30)

    tk.Label(frame, text="Username:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=300)
    username_entry = tk.Entry(frame, border=3, width=35)
    username_entry.place(x=180, y=300, height=30)

    tk.Label(frame, text="Password:", font=("Times New Roman", 14), bg="#ddd6f3").place(x=80, y=350)
    password_entry = tk.Entry(frame, border=3, width=35, show="*")
    password_entry.place(x=180, y=350, height=30)

    tk.Button(frame, text="Create Account", font=("Arial"), width=20, bg="black", fg="white",
              command=lambda: register_user(
                  full_name_entry.get(), address_entry.get(), email_entry.get(),
                  gender_var.get(), mobile_entry.get(), username_entry.get(), password_entry.get()
              )).place(x=125, y=430)

    back_to_login = tk.Label(master, text="Already have an account? Login", font=("Times New Roman", 10), fg="blue", bg="#ddd6f3", cursor="hand2")
    back_to_login.place(x=690, y=680)
    back_to_login.bind("<Button-1>", lambda e: login.create_login_frame(master))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.state('zoomed')
    show_registration_frame(root)
    root.mainloop()
