import tkinter as tk
def press(key):
    current = entry_var.get()
    current += str(key)
    entry_var.set(current)

def evaluate():
    try:
        result = eval(entry_var.get())  # Evaluate the expression entered by the user
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

def clear():
    entry_var.set("")

window = tk.Tk()
window.title("Calculator")


entry_var = tk.StringVar()


entry = tk.Entry(window, textvariable=entry_var, font=("Arial", 16), bd=10, relief="sunken", width=25, justify="right")
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=evaluate)
    elif text == "C":
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=clear)
    else:
        button = tk.Button(window, text=text, font=("Arial", 14), width=5, height=2, command=lambda key=text: press(key))
    
    button.grid(row=row, column=col)

# Run the main event loop
window.mainloop()
