import tkinter as tk
from PIL import Image, ImageTk

def show_remedies_precautions(root, result):
    for widget in root.winfo_children():
        widget.destroy()

   
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()

    bg_image = Image.open("h2.jpg")
    bg_image = bg_image.resize((w, h), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.place(x=0, y=0, width=w, height=h)

    title_label = tk.Label(root, text="Remedies and Precautions", font=("Arial", 24, "bold"), fg="white", bg="#1f4e78")
    title_label.place(x=0, y=0, width=w, height=50)

    frame_width = int(w * 0.6)
    frame_height = int(h * 0.5)
    frame_x = (w - frame_width) // 2  
    frame_y = int(h * 0.15)

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="black")


    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.place(x=frame_x, y=frame_y, width=frame_width, height=frame_height)
    scrollbar.place(x=frame_x + frame_width - 10, y=frame_y, height=frame_height)

    if result == "positive":
        content_title = "Treatment for Positive Result"
        content_text = (
            "1. Lifestyle Modifications:\n"
            "   - Adopt a heart-healthy diet rich in vegetables, fruits, whole grains, and lean proteins.\n"
            "   - Engage in regular physical activity like walking, jogging, or yoga.\n"
            "   - Avoid smoking and limit alcohol consumption.\n"
            "   - Manage stress through mindfulness, meditation, or hobbies.\n\n"
            
            "2. Medications:\n"
            "   - Cholesterol-lowering drugs: Statins to reduce bad cholesterol (LDL).\n"
            "   - Blood pressure medications: ACE inhibitors, beta blockers, or diuretics.\n"
            "   - Blood thinners: Aspirin or anticoagulants to prevent clots.\n"
            "   - Nitroglycerin: To relieve chest pain (angina).\n\n"
            
            "3. Medical Procedures and Surgeries:\n"
            "   - Angioplasty and Stenting: Open blocked arteries and restore blood flow.\n"
            "   - Coronary Artery Bypass Surgery (CABG): Create a new route for blood flow around blocked arteries.\n"
            "   - Pacemaker Implantation: Regulate irregular heartbeats.\n"
            "   - Valve Repair or Replacement: Treat damaged heart valves.\n\n"
            
            "4. Regular Monitoring and Check-Ups:\n"
            "   - Schedule regular visits to a cardiologist for monitoring.\n"
            "   - Perform routine tests like ECG, stress tests, and cholesterol checks.\n\n"
            
            "5. Cardiac Rehabilitation:\n"
            "   - A supervised program to improve cardiovascular health after surgery or a heart attack.\n\n"
            
            "6. Emergency Care:\n"
            "   - Recognize symptoms like chest pain, shortness of breath, or dizziness and seek immediate medical attention if they occur."
        )
    else:
        content_title = "Precautions for Negative Result"
        content_text = (
            "1. Maintain a balanced diet to keep your heart healthy.\n"
            "2. Engage in regular physical activity, such as walking or swimming.\n"
            "3. Monitor blood pressure and cholesterol levels periodically.\n"
            "4. Avoid unhealthy habits like smoking or excessive alcohol consumption.\n"
            "5. Manage stress through mindfulness, hobbies, or spending time with loved ones."
        )

    content_title_label = tk.Label(scrollable_frame, text=content_title, font=("Arial", 20, "bold"), fg="white", bg="black")
    content_title_label.pack(pady=10, anchor="w", padx=10)
    
    if result == "positive":
        precautions_button = tk.Button(
            root,
            text="Show Precautions",
            font=("Arial", 16),
            bg="#5bfd2d",
            fg="black",
            command=lambda: show_remedies_precautions(root, "negative")  # Show precautions
        )
        precautions_button.place(relx=0.5, rely=0.8, anchor="center", width=180, height=40)
        
    else:
        remidies_button = tk.Button(
            root,
            text="Show Remidies",
            font=("Arial", 16),
            bg="#e0fd2d",
            fg="black",
            command=lambda: show_remedies_precautions(root, "positive")  # Show precautions
        )
        remidies_button.place(relx=0.5, rely=0.8, anchor="center", width=180, height=40)

    content_text_label = tk.Label(scrollable_frame, text=content_text, font=("Arial", 14), fg="white", bg="black", justify="left", wraplength=frame_width - 40)
    content_text_label.pack(pady=10, anchor="w", padx=10)

    back_button = tk.Button(root, text="Back to Master Page", font=("Arial", 16), bg="#96b3e9", fg="black", command=lambda: go_back_to_master(root))
    back_button.pack(side="bottom", pady=80)

def go_back_to_master(root):
    root.destroy()
    import master
    master.root.mainloop()
