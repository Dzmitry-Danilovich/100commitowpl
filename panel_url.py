import  tkinter as tk
from tkinter import simpledialog

def enter_url():
    root = tk.Tk()
    root.withdraw()

    input_url = simpledialog.askstring("URL", "wprowadź url:")

    if input_url:
        return input_url
