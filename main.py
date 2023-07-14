from typing import Any
from collections.abc import Callable

import tkinter
from tkinter import ttk


def make_frame(root:tkinter.Tk, on_quit: Callable[[], Any]):
    """
    Tkのフレームをつくります
    """
    frm = ttk.Frame(root, padding=10)
    frm.grid(padx=10, pady=10)

    ttk.Label(
        frm,
        text="Hello World!",
        font=("Helvetica", 20, "bold"),
        # foreground="#ff0000",
    ).grid(column=0, row=0, pady=20)

    ttk.Button(
        frm,
        text="Quit",
        command=on_quit
    ).grid(column=0, row=1)


if __name__ == '__main__':
    root = tkinter.Tk()
    make_frame(root, root.destroy)
    root.mainloop()
