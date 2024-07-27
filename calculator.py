from tkinter import Tk, Entry, Button, StringVar
import math

class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        master.geometry("350x500")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(width=17, bg="#fff", font=("Arial Bold", 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ("(", 0, 50), (")", 90, 50), ("%", 180, 50), ("1", 0, 125),
            ("2", 90, 125), ("3", 180, 125), ("4", 0, 200), ("5", 90, 200),
            ("6", 180, 200), ("7", 0, 275), ("8", 90, 275), ("9", 180, 275),
            ("0", 0, 350), (".", 90, 350), ("+", 180, 350), ("-", 270, 350),
            ("/", 270, 200), ("*", 270, 50), ("^", 270, 350), ("=", 270, 125),
            ("C", 270, 275), ("sin", 0, 425), ("cos", 90, 425), ("tan", 180, 425),("log",270,425)
        ]

        for (text, x, y) in buttons:
            if text == "=":
                self.create_button(text, x, y, self.solve)
            elif text == "C":
                self.create_button(text, x, y, self.clear)
            else:
                self.create_button(text, x, y, lambda t=text: self.show(t))

    def create_button(self, text, x, y, command):
        Button(width=11, height=4, text=text, relief="flat", bg="white", command=command).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ""
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value, {"__builtins__": None}, {"math": math, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log":math.log})
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
