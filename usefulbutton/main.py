import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Useless Button", "This button does nothing!")

# Create the main application window
root = tk.Tk()
root.title("Useless Button")

# Create a button widget
button = tk.Button(root, text="Useless Button", command=on_button_click)
button.pack(pady=20)

# Run the application
root.mainloop()