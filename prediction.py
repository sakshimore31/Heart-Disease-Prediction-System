import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from subprocess import call

def Detect():
    e1=age.get()
    print(e1)
    e2=sex.get()
    print(e2)
    e3=cp.get()
    print(e3)
    e4=trestbps.get()
    print(e4)
    e5=chol.get()
    print(e5)
    e6=fbs.get()
    print(e6)
    e7=restecg.get()
    print(e7)
    e8=thalach.get()
    print(e8)
    e9=exang.get()
    print(e9)
    e10=oldpeak.get()
    print(e10)
    e11=slope.get()
    print(e11)
    e12=ca.get()
    print(e12)
    e13=thal.get()
    print(e13)
    
    
    from joblib import dump, load
    a1= load('SVM.joblib')
    v= a1.predict([[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13]])
    print(v)
    if v[0]==0:
        print("Heart Disease Detected")
        yes = tk.Label(root, text="Heart Disease Detected", bg="red", fg="black",font=("Harrington", 20, "bold"))
        yes.place(x=600, y=350)
        
    if v[0]==1:
        print("Heart Disease Not Detected")
        yes = tk.Label(root, text= "Heart Disease Not Detected", bg="green", fg="white",font=("Harrington", 20, "bold"))
        yes.place(x=600, y=350)


root = tk.Tk()
root.title("Prediction Input")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}")
root.state('zoomed')




bg_image = Image.open("h2.jpg")
bg_image = bg_image.resize((w, h), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.image = bg_image
bg_label.place(x=0, y=0, width=w, height=h)

title_label = tk.Label(root, text="Prediction Page", font=("Arial", 28, "bold"), fg="white", bg="black")
title_label.place(x=0, y=0, width=w, height=40)


age = tk.IntVar()
sex = tk.IntVar()
cp = tk.IntVar()
trestbps = tk.IntVar()
chol = tk.IntVar()
fbs = tk.IntVar()
restecg = tk.IntVar()
thalach = tk.IntVar()
exang = tk.IntVar()
oldpeak = tk.IntVar()
slope = tk.IntVar()
ca = tk.IntVar()
thal = tk.IntVar()
target = tk.IntVar()


fields = [
    ("Age", age),
    ("Sex", sex),
    ("Chest Pain Type (cp)", cp),
    ("Resting Blood Pressure\n (trestbps)", trestbps),
    ("Serum Cholesterol (chol)", chol),
    ("Fasting Blood Sugar (fbs)", fbs),
    ("Resting Electrocardiographic\n Results (restecg)", restecg),
    ("Max Heart Rate Achieved\n (thalach)", thalach),
    ("Exercise-Induced\n Angina (exang)", exang),
    ("ST Depression (oldpeak)", oldpeak),
    ("Slope of Peak Exercise\n ST Segment (slope)", slope),
    ("Number of Major\n Vessels (ca)", ca),
    ("Thalassemia (thal)", thal),
    ("Target", target)
]



input_frame = tk.Frame(root, bg="#33ccff", relief="raised", bd=3)
input_frame.place(x=80, y=80, width=450, height=670)


for i, (label_text, var) in enumerate(fields):
    label = tk.Label(input_frame, text=label_text, font=("Arial", 12, "italic"), bg="#33ccff")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry = ttk.Entry(input_frame, textvariable=var, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")


predict_button = tk.Button(
    input_frame, text="Detect", command=Detect, bg="green", fg="white", font=("Times New Roman", 16, "bold")
)
predict_button.grid(row=len(fields), column=0, columnspan=2, pady=10)



root.mainloop()