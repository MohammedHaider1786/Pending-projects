import tkinter as tk
import random

# Function to decide winner
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = f"Draw! Both chose {user_choice}"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {user_choice} beats {computer_choice}"
    else:
        result = f"You Lose! {computer_choice} beats {user_choice}"

    result_label.config(text=result)


# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=20)

# Run the game
root.mainloop()
