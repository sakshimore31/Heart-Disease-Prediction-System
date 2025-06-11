from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA    #principle categorical analysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from tkinter import messagebox
from remedies_precautions import show_remedies_precautions
import subprocess
from remedies_precautions import show_remedies_precautions


def Data_Preprocessing():
    data=pd.read_csv("heart.csv")
    data.head()
    
    data = data.dropna()
    le= LabelEncoder() #converts textual data into numeric values
    data['age'] = le.fit_transform(data['age']) #scaling process
    data['sex'] = le.fit_transform(data['sex'])
    data['cp'] = le.fit_transform(data['cp'])
    data['trestbps'] = le.fit_transform(data['trestbps'])
    data['chol'] = le.fit_transform(data['chol'])
    data['fbs'] = le.fit_transform(data['fbs'])
    data['restecg'] = le.fit_transform(data['restecg'])
    data['thalach'] = le.fit_transform(data['thalach'])
    data['exang'] = le.fit_transform(data['exang'])
    data['oldpeak'] = le.fit_transform(data['oldpeak'])
    data['slope'] = le.fit_transform(data['slope'])
    data['ca'] = le.fit_transform(data['ca'])
    data['thal'] = le.fit_transform(data['thal'])
    data['target'] = le.fit_transform(data['target'])
    
    '''Feature selection'''
    
    x=data.drop(['age'], axis=1)
    data = data.dropna()
    
    print(type(x))
    y= data['age']
    print(type(y))
    x.shape
    
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20)
    load = tk.Label(root,font=("Tempus sans ITC", 15, "bold"), width=50, height=1, background="black", foreground="white", text="Data Loaded=> Splitted into 80% for training & 20% for Testing")
    load.place(x=570,y=100)
    

def Model_Training():
    data =pd.read_csv("heart.csv")
    data.head()
    
    data= data.dropna()
    le= LabelEncoder() #converts texual data into numeric values
    data['age'] = le.fit_transform(data['age']) #scaling process
    data['sex'] = le.fit_transform(data['sex'])
    data['cp'] = le.fit_transform(data['cp'])
    data['trestbps'] = le.fit_transform(data['trestbps'])
    data['chol'] = le.fit_transform(data['chol'])
    data['fbs'] = le.fit_transform(data['fbs'])
    data['restecg'] = le.fit_transform(data['restecg'])
    data['thalach'] = le.fit_transform(data['thalach'])
    data['exang'] = le.fit_transform(data['exang'])
    data['oldpeak'] = le.fit_transform(data['oldpeak'])
    data['slope'] = le.fit_transform(data['slope'])
    data['ca'] = le.fit_transform(data['ca'])
    data['thal'] = le.fit_transform(data['thal'])
    data['target'] = le.fit_transform(data['target'])
    
    x=data.drop(['target'], axis=1)
    data=data.dropna()
    
    print(type(x))
    y=data['target']
    print(type(y))
    x.shape
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)
    
    from sklearn.svm import SVC
    svcclassifier =SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)  
    y_pred =svcclassifier.predict(x_test)
    print(y_pred)
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ", (classification_report(y_test, y_pred)))
    print("Accuracy : ", accuracy_score(y_test, y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy : %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root, text = str(repo), width=45,height=10, bg="#FFFDD0", fg="black", font=("ROBOTO",14))
    label4.place(x=570, y=140)
    
    label5 = tk.Label(root, text="Accuracy : "+str(ACC)+"%\nModel saved as SVM.joblib", width=45, height=5, bg="#FFFDD0", fg="black", font=("ROBOTO",14))
    label5.place(x=570, y= 350)
    from joblib import dump
    dump (svcclassifier, "SVM.joblib")
    print("Model saved as SVM.joblib")
    
   

def check_prediction():
    call(["python","prediction.py"])
    

def logout():
    root.destroy()
    subprocess.call(['python', 'home.py'])
    
    
root = tk.Tk()
root.title("Heart Disease Detection")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{w}x{h}")
root.state('zoomed')



bg_image = Image.open("h2.jpg")  
bg_image = bg_image.resize((w, h), Image.LANCZOS)
bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


title_label = tk.Label(root, text="Heart Disease Detection System using SVM", 
                       font=("Arial", 28, "bold"), fg="black", bg="#94bbe9")
title_label.place(x=0, y=0, width=w, height=70)


button_frame = tk.Frame(root, bg="black", relief="groove", bd=5)
button_frame.place(relx=0.78, rely=0.35, anchor="w", width=350, height=370)


data_button = tk.Button(button_frame, text="Data preprocessing", font=("Arial", 18, "bold"), 
                        bg="#96b3e9", fg="white", command=Data_Preprocessing)
data_button.pack(pady=10, fill="x", padx=30)


train_button = tk.Button(button_frame, text="Model Training", font=("Arial", 18, "bold"), 
                         bg="#96b3e9", fg="white", command=Model_Training)
train_button.pack(pady=10, fill="x", padx=30)


predict_button = tk.Button(button_frame, text="Check Prediction", font=("Arial", 18, "bold"), 
                            bg="#96b3e9", fg="white", command=check_prediction)
predict_button.pack(pady=10, fill="x", padx=30)

remedies_button = tk.Button(button_frame, text="Remedies & Precautions", 
                            font=("Arial", 18, "bold"), bg="#96b3e9", fg="white", 
                            command=lambda: show_remedies_precautions(root, "positive"))
remedies_button.pack(pady=10, fill="x", padx=30)

logout_button = tk.Button(button_frame, text="Logout", font=("Arial", 18, "bold"), 
                           bg="#96b3e9", fg="white", command=logout)
logout_button.pack(pady=10, fill="x", padx=30)


root.mainloop()
