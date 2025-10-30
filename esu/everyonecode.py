#لينك الفيديو التعليمي 
#https://youtu.be/GX03n-qDhmE
#لينك مشاركة الحل في تويتر 
#https://twitter.com/Sara_amrey/status/1678198588826845187?s=20


import random

number = random.randint(1, 5)
guess = 0

while guess != number:
    guess = int(input("ادخل تخمينك: "))
    if guess == number:
        print("تهانينا! لقد قمت بتخمين الرقم بشكل صحيح.")
    else:
        print("تخمين خاطئ. حاول مرة أخرى!")


























'''
import tkinter as tk
from random import randint

number = randint(1, 5)

def check_guess():
    guess = int(entry.get())
    if guess == number:
        label.config(text="Congratulations! You guessed the number correctly.")
    else:
        label.config(text="Wrong guess. Try again!")

root = tk.Tk()
root.title("Number Guessing Game")

label = tk.Label(root, text="Guess a number between 1 and 5")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=check_guess)
button.pack()

root.mainloop()
'''
