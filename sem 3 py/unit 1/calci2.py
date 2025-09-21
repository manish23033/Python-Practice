import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to evaluate the expression
def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the input field
def button_clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying input
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3)
]

# Create number and operation buttons
for (text, row, col) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 14),
              command=lambda text=text: button_click(text)).grid(row=row, column=col)

# Equal button
tk.Button(root, text="=", width=5, height=2, font=('Arial', 14), command=button_equal).grid(row=4, column=2)

# Clear button
tk.Button(root, text="C", width=5, height=2, font=('Arial', 14), command=button_clear).grid(row=4, column=0)

# Run the main loop
root.mainloop()
