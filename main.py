from typing import Any
from collections.abc import Callable

import tkinter
from tkinter import ttk

from hello import game


def make_frame(root: tkinter.Tk, on_quit: Callable[[], Any]) -> None:
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

    ttk.Button(frm, text="Boot", command=game.boot).grid(column=0, row=1)

    ttk.Button(frm, text="Quit", command=on_quit).grid(column=0, row=2)


if __name__ == "__main__":
    root = tkinter.Tk()
    make_frame(root, root.destroy)
    root.mainloop()
