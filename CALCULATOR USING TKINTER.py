from tkinter import *

def click(button_text):
    current = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, current + button_text)

def clear():
    entry_box.delete(0, END)

def calculate():
    try:
        result = eval(entry_box.get())
        entry_box.delete(0, END)
        entry_box.insert(0, str(result))
    except:
        entry_box.delete(0, END)
        entry_box.insert(0, "Error")

# Main window
window = Tk()
window.title("Simple Calculator")
window.geometry("300x400")

entry_box = Entry(window, width=25, font=("Arial", 18), justify="right")
entry_box.pack(pady=10)

# Buttons Frame
frame = Frame(window)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for button in buttons:
    def make_lambda(x=button):
        return lambda: click(x) if x != "=" else calculate()

    btn = Button(frame, text=button, width=5, height=2,
                 font=("Arial", 14),
                 command=make_lambda())
    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        row += 1
        col = 0

clear_btn = Button(window, text="CLEAR", width=20, height=2,
                   font=("Arial", 14), command=clear)
clear_btn.pack(pady=10)

window.mainloop()
