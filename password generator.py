import tkinter as tk
import random
import string

# Function to generate a password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Enter a positive number")
            return
    except ValueError:
        result_label.config(text="Enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"Generated Password: {password}")


# GUI setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", wraplength=350)
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
