from tkinter import *
from tkinter import ttk


def make_frame(root: Tk):
    """
    Tkのフレームをつくります
    """
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=1)


if __name__ == '__main__':
    root = Tk()
    make_frame(root)
    root.mainloop()
