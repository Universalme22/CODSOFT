import tkinter as tk
from tkinter import messagebox

questions = [
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], "Paris"),
    ("What is 5 + 7?", ["10", "12", "13", "15"], "12"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Saturn"], "Mars"),
    ("Who wrote 'Hamlet'?", ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"], "William Shakespeare"),
    ("What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific")
]


current_question = 0
score = 0


def load_question():
    global current_question
    if current_question < len(questions):
        question_label.config(text=questions[current_question][0])
        for i, option in enumerate(questions[current_question][1]):
            option_buttons[i].config(text=option)
    else:
        show_result()


def check_answer(selected_option):
    global current_question, score
    if questions[current_question][2] == selected_option:
        score += 1
    current_question += 1
    load_question()


def show_result():
    messagebox.showinfo("Quiz Result", f"You scored {score} out of {len(questions)}")
    root.quit()


root = tk.Tk()
root.title("Quiz Game")
root.geometry("500x400")
root.configure(bg="#f0f0f0")


question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f0f0")
question_label.pack(pady=20)


option_buttons = []
for i in range(4):
    button = tk.Button(root, text="", font=("Helvetica", 14), width=20, command=lambda option=i: check_answer(option_buttons[option].cget("text")))
    button.pack(pady=10)
    option_buttons.append(button)


load_question()


root.mainloop()
