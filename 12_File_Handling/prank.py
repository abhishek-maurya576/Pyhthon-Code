import tkinter as tk
from tkinter import messagebox
import threading
import time
import winsound
import pyautogui
import random

# --- Blue Screen Simulation ---
def show_bsod():
    bsod = tk.Toplevel()
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="blue")

    label = tk.Label(bsod, text=":(\nYour PC ran into a problem and needs to restart.\nWe're just collecting some error info, and then we'll restart for you.",
                     font=("Consolas", 20), fg="white", bg="blue", justify="left")
    label.pack(pady=100)

    percent = tk.Label(bsod, text="0% complete", font=("Consolas", 18), fg="white", bg="blue")
    percent.pack()

    for i in range(101):
        percent.config(text=f"{i}% complete")
        time.sleep(0.05)

    bsod.destroy()

# --- Red blinking background ---
def red_blink():
    while True:
        root.configure(bg="darkred")
        time.sleep(0.3)
        root.configure(bg="black")
        time.sleep(0.3)

# --- Fake formatting ---
def fake_formatting():
    for i in range(101):
        progress_var.set(i)
        status_label.config(text=f"Formatting C:\\System32... {i}%")
        time.sleep(0.07)
    winsound.Beep(1000, 500)
    messagebox.showwarning("System32 Deleted", "Critical error: Format Complete 🔥")
    show_bsod()
    messagebox.showinfo("😜 Just Kidding!", "Relax bro... It's just a prank 😄")
    root.destroy()

# --- Fake random mouse move ---
def crazy_mouse():
    screen_w, screen_h = pyautogui.size()
    for _ in range(100):
        x = random.randint(0, screen_w - 1)
        y = random.randint(0, screen_h - 1)
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(0.1)

# --- Setup Main Window ---
root = tk.Tk()
root.title("System Prank Suite")
root.attributes("-fullscreen", True)
root.configure(bg="black")

status_label = tk.Label(root, text="Initializing system breach...", fg="red", bg="black", font=("Courier", 24))
status_label.pack(pady=50)

progress_var = tk.IntVar()
progress_bar = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=progress_var,
                        length=600, showvalue=False, troughcolor="red", fg="white",
                        sliderlength=30, highlightthickness=0, bd=0, bg="black")
progress_bar.pack(pady=20)

# Start threads
threading.Thread(target=red_blink, daemon=True).start()
threading.Thread(target=crazy_mouse, daemon=True).start()
threading.Thread(target=fake_formatting).start()

# Exit with ESC
root.bind("<Escape>", lambda e: root.destroy())
root.mainloop()
