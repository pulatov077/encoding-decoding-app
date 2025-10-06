"""Encoding-Decoding App (GUI Version)

This module provides a graphical user interface (GUI) for encoding and
decoding text
using various methods: Base64, Hex, ROT13, and URL encoding.
Author: Pulatov Ziyo
Year: 2025
"""

import base64
import codecs
import urllib.parse
import tkinter as tk
from tkinter import ttk, messagebox


def encode_text(text: str, method: str = "base64") -> str:
    """Encode given text using the selected method.

    Args:
        text (str): Text to encode.
        method (str): Encoding method ("base64", "hex", "rot13", "url").

    Returns:
        str: Encoded text or error message.
    """
    if method == "base64":
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    if method == "hex":
        return text.encode("utf-8").hex()
    if method == "rot13":
        return codecs.encode(text, "rot_13")
    if method == "url":
        return urllib.parse.quote(text)
    return "❌ Noto'g'ri usul!"


def decode_text(text: str, method: str = "base64") -> str:
    """Decode text using the selected method.

    Args:
        text (str): Encoded text to decode.
        method (str): Decoding method ("base64", "hex", "rot13", "url").

    Returns:
        str: Decoded text or error message.
    """
    try:
        if method == "base64":
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        if method == "hex":
            return bytes.fromhex(text).decode("utf-8")
        if method == "rot13":
            return codecs.decode(text, "rot_13")
        if method == "url":
            return urllib.parse.unquote(text)
        return "❌ Noto'g'ri usul!"
    except Exception as error:
        return f"❌ Xatolik: {str(error)}"


def process(mode: str, text_widget, method_var, output_widget):

    """Handle encoding or decoding process based on user selection."""
    text = text_widget.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Xatolik", "Matn kiriting!")
        return

    method = method_var.get()
    if mode == "encode":
        result = encode_text(text, method)
    else:
        result = decode_text(text, method)

    output_widget.delete("1.0", tk.END)
    output_widget.insert(tk.END, result)



def create_gui():
    """Create and run the GUI application."""
    root = tk.Tk()
    root.title("🔐 Encoding-Decoding App (GUI)")
    root.geometry("600x500")
    root.resizable(False, False)

    # --- Input Section ---
    tk.Label(root, text="Matn kiriting:", font=("Arial", 12)).pack(pady=(10, 0))
    input_box = tk.Text(root, height=6, font=("Consolas", 11))
    input_box.pack(fill="x", padx=15, pady=5)

    # --- Method Selection ---
    method_var = tk.StringVar(value="base64")
    tk.Label(root, text="Usulni tanlang:", font=("Arial", 11)).pack()
    method_menu = ttk.Combobox(
        root,
        textvariable=method_var,
        values=["base64", "hex", "rot13", "url"],
        state="readonly",
    )
    method_menu.pack(pady=5)

    # --- Buttons ---
    frame = tk.Frame(root)
    frame.pack(pady=10)
    tk.Button(
        frame,
        text="Encode",
        command=lambda: process("encode", input_box, method_var, output_box),
        width=15,
        bg="#4CAF50",
        fg="white",
    ).pack(side="left", padx=10)
    tk.Button(
        frame,
        text="Decode",
        command=lambda: process("decode", input_box, method_var, output_box),
        width=15,
        bg="#2196F3",
        fg="white",
    ).pack(side="left", padx=10)

    # --- Output Section ---
    tk.Label(root, text="Natija:", font=("Arial", 12)).pack()
    output_box = tk.Text(root, height=6, font=("Consolas", 11))
    output_box.pack(fill="x", padx=15, pady=5)

    # --- Footer ---
    tk.Label(
        root,
        text="© 2025 Encoding-Decoding App | by Pulatov Ziyo",
        font=("Arial", 9),
        fg="gray",
    ).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()

# type: ignore