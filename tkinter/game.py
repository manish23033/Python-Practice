import tkinter as tk
import random
import time

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the Button Game")
        self.root.geometry("400x300")

        # Initialize variables
        self.clicks = 0
        self.time_left = 10
        self.is_game_over = False

        # Create a label for displaying instructions or score
        self.label = tk.Label(root, text="Click the button as many times as you can in 10 seconds!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Create the button
        self.button = tk.Button(root, text="Click Me!", font=("Arial", 14), command=self.button_click)
        self.button.pack(pady=20)

        # Create a timer label
        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.pack(pady=10)

        # Start the countdown timer
        self.update_timer()

    def button_click(self):
        if not self.is_game_over:
            self.clicks += 1

    def update_timer(self):
        if self.time_left > 0 and not self.is_game_over:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(1000, self.update_timer)  # Call this function again after 1 second
        else:
            self.is_game_over = True
            self.show_result()

    def show_result(self):
        self.label.config(text=f"Game Over! You clicked {self.clicks} times.")
        self.button.config(state=tk.DISABLED)  # Disable the button after game ends

# Create the Tkinter window
root = tk.Tk()

# Initialize the game
game = ClickGame(root)

# Start the Tkinter event loop
root.mainloop()
