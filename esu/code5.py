import tkinter as tk
from tkinter import messagebox

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def check_prime():
    input_value = entry.get()
    try:
        num = int(input_value)
        if num <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
        else:
            if is_prime(num):
                messagebox.showinfo("Result", f"{num} is a prime number.")
            else:
                messagebox.showinfo("Result", f"{num} is not a prime number.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a positive integer.")

# Create the main window
root = tk.Tk()
root.title("Prime Number Checker")

# Create and place widgets
label = tk.Label(root, text="Enter a positive integer:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=check_prime)
check_button.pack()

# Start the main loop
root.mainloop()
