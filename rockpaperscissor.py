import random
import tkinter as tk
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_label.config(text=f"You: {user_choice}\nComputer: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

root = tk.Tk()
root.title("Rock Paper Scissors")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack()
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack()

for choice in choices:
    tk.Button(root, text=choice, font=("Arial", 12), command=lambda c=choice: play(c)).pack()

root.mainloop()
