
import os
import time
from tkinter import Tk, Label

# -----------------------------
# CONFIGURATION
# -----------------------------
URGENT_FOLDER = r"C:\Users\Usuario\Desktop\notif"  # <-- Change this to your shared folder path
CHECK_INTERVAL = 15  # in seconds

# Track files we've already seen
seen_files = set()

def show_popup(message):
    root = Tk()
    root.title("⚠️ ALERTA DE AUDIO URGENTE ⚠️")
    root.geometry("700x200+400+300")  # Width x Height + X + Y
    root.attributes("-topmost", True)
    root.configure(bg="yellow")

    label = Label(root, text=message, font=("Arial", 18, "bold"), bg="yellow", fg="black", wraplength=650, justify="center")
    label.pack(expand=True, fill="both", padx=20, pady=20)

    root.mainloop()

def check_folder():
    global seen_files
    try:
        current_files = set(os.listdir(URGENT_FOLDER))
        new_files = current_files - seen_files
        if new_files:
            file_list = "\n".join(new_files)
            show_popup(f"Nuevo audio URGENTE recibido:\n{file_list}")
        seen_files.update(new_files)
    except Exception as e:
        print("Error checking folder:", e)

def main():
    print("Monitoring urgent folder for new files...")
    while True:
        check_folder()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
