import tkinter as tk
from tkinter import messagebox
import random

# Mapping words to clues
word_clues = {
    'python': 'A widely used high-level programming language.',
    'java': 'A popular programming language that is concurrent, class-based, and object-oriented.',
    'kotlin': 'A statically typed programming language that runs on the JVM and is used for Android development.',
    'javascript': 'A high-level, just-in-time compiled language that conforms to the ECMAScript specification.',
    'ruby': 'A dynamic, open source programming language with a focus on simplicity and productivity.',
    'swift': 'A powerful programming language for iOS and macOS apps.',
    'hangman': 'A game where you guess the word letter by letter.'
}

words = list(word_clues.keys())
word = random.choice(words)
guessed_letters = set()
attempts = 6

# Initialize the main window
root = tk.Tk()
root.title("Hangman Game")

# Displaying the word and clue
word_display = tk.StringVar()
clue_display = tk.StringVar(value=f"Clue: {word_clues[word]}")


def update_word_display():
    displayed_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    word_display.set(displayed_word)


update_word_display()

# Updating attempts left
attempts_var = tk.StringVar()
attempts_var.set(f"Attempts left: {attempts}")


# Function to handle guessing
def guess():
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter or len(letter) > 1:
        messagebox.showwarning("Hangman", "Please enter a single letter.")
        return

    if letter in guessed_letters:
        messagebox.showinfo("Hangman", "You already guessed that letter.")
        return

    guessed_letters.add(letter)

    if letter not in word:
        attempts -= 1
        attempts_var.set(f"Attempts left: {attempts}")

    update_word_display()

    if attempts <= 0:
        messagebox.showinfo("Hangman", f"You lost! The word was: {word}")
        reset_game()
    elif "_" not in word_display.get():
        messagebox.showinfo("Hangman", "Congratulations, you won!")
        reset_game()


def reset_game():
    global word, guessed_letters, attempts
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    update_word_display()
    attempts_var.set(f"Attempts left: {attempts}")
    clue_display.set(f"Clue: {word_clues[word]}")


# Creating the GUI layout
clue_label = tk.Label(root, textvariable=clue_display, font=('Helvetica', 14))
clue_label.pack(pady=(10, 0))

label = tk.Label(root, textvariable=word_display, font=('Helvetica', 24))
label.pack(pady=20)

entry = tk.Entry(root, font=('Helvetica', 24))
entry.pack(pady=20)

guess_button = tk.Button(root, text="Guess", command=guess)
guess_button.pack(pady=20)

attempts_label = tk.Label(root, textvariable=attempts_var, font=('Helvetica', 14))
attempts_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=20)

root.mainloop()
