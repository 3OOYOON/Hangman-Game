#Author: 3OOYOON

import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font

dictionaryFile = "phrase.txt"

# Create the main window
window = tk.Tk()
window.title("Letter Guessing Game")
window.configure(bg='#006600')  

# Custom font
my_font = font.Font(family='Courier', size=12, weight='bold')

def resize_event(event):
    outer_frame.configure(width=event.width, height=event.height)

# Create and configure an outer frame (border)
outer_frame = tk.Frame(window, bg='#00CC00', bd=2, relief='flat')  
outer_frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
outer_frame.bind('<Configure>', resize_event)

# Create and configure an inner frame (content area)
inner_frame = tk.Frame(outer_frame, bg='#00CC00')  
inner_frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

class LetterGuessGame:
    def __init__(self, master):
        self.master = master

        # Create and configure an inner frame (content area) for the game
        game_frame = tk.Frame(self.master, bg='#00CC00')  
        game_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.instruction_label = tk.Label(game_frame, text='Guess the phrase, you have 15 guesses.', bg='#00CC00', fg='#FFFFFF', font=my_font)
        self.instruction_label.grid(row=0, column=0, pady=5)

        self.unknown_label = tk.Label(game_frame, text="", font=my_font)
        self.unknown_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.guess_entry = tk.Entry(game_frame)
        self.guess_entry.grid(row=2, column=0, pady=5)

        self.guess_button = tk.Button(game_frame, text="Guess", command=self.make_guess)
        self.guess_button.grid(row=3, column=0, pady=5)

        self.reset_button = tk.Button(game_frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, pady=5)

        self.max_guesses = 15
        self.guess_history = 0
        self.chosen_phrase = self.choose_phrase()
        self.letters = list(self.chosen_phrase.lower())
        self.unknown = '_' * len(self.chosen_phrase)

        self.remaining_guesses = self.max_guesses
        self.update_unknown_label()

    def choose_phrase(self):
        with open(dictionaryFile, 'r') as f:
            phrases = f.readlines()
        return random.choice(phrases).strip()

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if not guess.isalpha() or len(guess) != 1:
            messagebox.showwarning("Invalid Guess", "Please enter a valid single letter.")
            return

        self.guess_history += 1

        if guess not in self.letters:
            messagebox.showinfo("Incorrect Guess", "That letter is not in the phrase. Try again.")
        else:
            self.unknown = ''.join([chosen if chosen == guess else blank for chosen, blank in zip(self.letters, self.unknown)])

        self.remaining_guesses -= 1
        self.update_unknown_label()
        self.update_instruction_label()

        if '_' not in self.unknown:
            won_message = f"Congratulations! You guessed the phrase: '{self.chosen_phrase}'"
            messagebox.showinfo("Congratulations", won_message)
            self.disable_guessing()

        elif self.remaining_guesses <= 0:
            lost_message = f"Game Over! You couldn't guess the phrase.\n\nThe correct phrase was:\n'{self.chosen_phrase}'"
            messagebox.showinfo("Game Over", lost_message)
            self.disable_guessing()

    def update_unknown_label(self):
        self.unknown_label.config(text=self.unknown)

    def update_instruction_label(self):
        self.instruction_label.config(text=f'Guess the phrase, you have {self.remaining_guesses} guesses.')

    def reset_game(self):
        self.guess_history = 0
        self.remaining_guesses = self.max_guesses
        self.chosen_phrase = self.choose_phrase()
        self.letters = list(self.chosen_phrase.lower())
        self.unknown = '_' * len(self.chosen_phrase)
        self.update_unknown_label()
        self.update_instruction_label()
        self.enable_guessing()

    def disable_guessing(self):
        self.guess_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)

    def enable_guessing(self):
        self.guess_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)


if __name__ == "__main__":
    game = LetterGuessGame(inner_frame)
    window.mainloop()
