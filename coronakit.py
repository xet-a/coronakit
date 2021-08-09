import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import webbrowser

def center_window(root, w, h):
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw/2) - (w/2)
    y = (sh/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def callback():
    webbrowser.open_new("http://www.google.com")

def main() :
    root = tk.Tk()
    root.title('[PROJECT] coronakit')
    center_window(root, 1200, 770)
    root.resizable(0,0)
    root.configure(bg='white')

    logo = Image.open("./assets/project.png").resize((300, 75), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    label = tk.Label(root, image=logo, borderwidth=0)
    label.pack(pady=(70,40))

    saved_as_excel = PhotoImage(file="./assets/excel.png")
    excel_button = tk.Button(root, image=saved_as_excel, borderwidth=0, highlightthickness=0, command=root.destroy)
    excel_button.pack(pady=(20,20))

    data_transfer = PhotoImage(file="./assets/data.png")
    data_button = tk.Button(root, image=data_transfer, borderwidth=0, highlightthickness=0, command=root.destroy)
    data_button.pack(pady=(10,20))

    to_site = PhotoImage(file="./assets/site.png")
    site_button = tk.Button(root, image=to_site, borderwidth=0, highlightthickness=0, command=callback)
    site_button.pack(pady=(10,20))

    exit = PhotoImage(file="./assets/exit.png")
    exit_button = tk.Button(root, image=exit, borderwidth=0, highlightthickness=0, command=root.destroy)
    exit_button.pack(pady=(10,0))

    help = PhotoImage(file="./assets/help.png")
    help_button = tk.Button(root, image=help, borderwidth=0, highlightthickness=0, command=root.destroy)
    help_button.pack(side="right", anchor="e", padx=(0,5), pady=(0,5))

    root.mainloop()

if __name__ == '__main__' :
    main()