import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from typing import Optional


def make_file(text: str, file_name: Optional[str] = None, path: Optional[str] = None) -> None:
    if not file_name:
        file_name = "file.txt"

    full_path = Path(path) / file_name if path else Path(file_name)
    full_path.parent.mkdir(parents=True, exist_ok=True)

    with open(full_path, "a", encoding="utf-8") as f:
        f.write(text)


def send_message(text: str, is_file: bool, button: tk.Button,
                 label: Optional[tk.Label] = None,
                 filename_entry: Optional[tk.Entry] = None,
                 filepath_entry: Optional[tk.Entry] = None) -> None:

    fname = filename_entry.get() if filename_entry else None
    fpath = filepath_entry.get() if filepath_entry else None
    button.destroy()

    if label:
        label.destroy()
    if filename_entry:
        filename_entry.destroy()
    if filepath_entry:
        filepath_entry.destroy()

    if is_file:
        make_file(text, fname, fpath)
    else:
        print(text)


def send_message_GUI(start_button: tk.Button):
    start_button.destroy()
    label = tk.Label(root, text="Please enter the text you want to send!")
    label.pack(pady=10)

    text_entry = tk.Entry(root, width=40)
    text_entry.pack(pady=10)

    label2 = tk.Label(root, text="Type Y/YES to save to file, N/NO to just print:")
    label2.pack(pady=10)

    want_file_entry = tk.Entry(root, width=20)
    want_file_entry.pack(pady=10)

    def continue_flow():
        text_value = text_entry.get().strip()
        choice = want_file_entry.get().strip().upper()

        if not text_value:
            messagebox.showerror("Error", "There needs to be text!")
            return

        if choice not in ("Y", "YES", "N", "NO"):
            messagebox.showerror("Error", "You must type Y/YES or N/NO.")
            return

        label.destroy()
        label2.destroy()
        text_entry.destroy()
        want_file_entry.destroy()
        next_button.destroy()

        if choice in ("Y", "YES"):
            label3 = tk.Label(root, text="Enter filename and optional path:")
            label3.pack(pady=10)

            filename_entry = tk.Entry(root, width=30)
            filename_entry.pack(pady=5)

            filepath_entry = tk.Entry(root, width=30)
            filepath_entry.pack(pady=5)

            send_btn = tk.Button(
                root,
                text="Send message!",
                command=lambda: send_message(
                    text_value,
                    True,
                    send_btn,
                    label3,
                    filename_entry,
                    filepath_entry,
                ),
            )
            send_btn.pack(pady=10)

        else:
            send_btn = tk.Button(
                root,
                text="Send message!",
                command=lambda: send_message(text_value, False, send_btn),
            )
            send_btn.pack(pady=10)

    next_button = tk.Button(root, text="Continue", command=continue_flow)
    next_button.pack(pady=10)

root = tk.Tk()
root.maxsize(555, 300)
root.title("Hello this is a test!")

start_btn = tk.Button(root, text="Send message!", command=lambda: send_message_GUI(start_btn))
start_btn.pack(pady=40)

root.mainloop()