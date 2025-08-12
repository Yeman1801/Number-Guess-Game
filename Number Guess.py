from tkinter import *
import random

root = Tk()
root.title("Number Guess Game")
root.geometry("300x250")

num = random.randint(1, 100)

tries = 7
low = 1
high = 100

def check():
    global tries, num, low, high
    
    try:
        g = int(t1.get())
    except ValueError:
        l2.config(text="Enter a valid number.", font=("Arial", 10))
        return

    tries -= 1

    if g == num:
        l2.config(text=f"Correct! Number was {num}.")
        b1.config(state="disabled")
    elif g < num:
        low = max(low, g + 1)
        l2.config(text=f"Too low! Try {low}-{high}. Tries left: {tries}")
    else:
        high = min(high, g - 1)
        l2.config(text=f"Too high! Try {low}-{high}. Tries left: {tries}")

    if tries <= 0 and g != num:
        l2.config(text=f"Out of tries. Number was {num}.")
        l2.config(text=f"you Loss")
        b1.config(state="disabled")

    t1.delete(0, END)


def restart():
    global num, tries, low, high
    num = random.randint(1, 100)
    tries = 7
    low = 1
    high = 100
    l2.config(text="Guess a number between 1 and 100")
    b1.config(state="normal")
    t1.delete(0, END)

l1 = Label(text="GUESS:", font=("Bahnschrift Condensed", 15))
l1.place(x=10, y=50)
t1 = Entry(font=("Bahnschrift SemiBold SemiCondensed", 12))
t1.place(x=90, y=52, width=100, height=30)

button = {"font": ("bold", 13), "bd": 7, "relief": "solid"}

b1 = Button(text="Guess", command=check, **button)
b1.place(x=40, y=150, width=100)

b2 = Button(text="Restart", command=restart, **button)
b2.place(x=160, y=150, width=100)

l2 = Label(text="Guess a number between 1 and 100", font=("Arial", 10))
l2.place(x=10, y=100)

root.mainloop()
