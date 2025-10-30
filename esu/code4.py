import tkinter as tk

def factorial(n):
    if n < 0:
        return "Please enter a non-negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def calculate_factorial():
    number = int(entry.get())
    result = factorial(number)
    result_label.config(text=f"{number}! = {result}")

# إنشاء نافذة الواجهة الرسومية
root = tk.Tk()
root.title("Factorial Calculator")

# إنشاء مربع إدخال لإدخال العدد
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# إنشاء زر لحساب مضروب العدد
calculate_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
calculate_button.pack()

# إنشاء علامة لعرض النتيجة
result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# تشغيل الواجهة الرسومية
root.mainloop()
