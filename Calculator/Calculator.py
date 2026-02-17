from tkinter import Tk, Frame, Label, Entry, Button, StringVar, DoubleVar

class Calculator:
    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("320x220")

        self.n1 = DoubleVar()
        self.n2 = DoubleVar()
        self.result = StringVar(value="Result:")

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
    
        Label(self.win, text="Number 1:").grid(row=0, column=0, sticky="w", padx=10, pady=(10, 2))
        Entry(self.win, width=20, textvariable=self.n1).grid(row=0, column=1, padx=10, pady=(10, 2))

        Label(self.win, text="Number 2:").grid(row=1, column=0, sticky="w", padx=10, pady=2)
        Entry(self.win, width=20, textvariable=self.n2).grid(row=1, column=1, padx=10, pady=2)

        Label(self.win, textvariable=self.result).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        btn_frame = Frame(self.win)
        btn_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        add_button = Button(btn_frame, text="+", width=4, command=self.add)
        add_button.grid(row=0, column=0, padx=2, pady=2)

        subtract_button = Button(btn_frame, text="-", width=4, command=self.subtract)
        subtract_button.grid(row=0, column=1, padx=2, pady=2)

        multiply_button = Button(btn_frame, text="×", width=4, command=self.multiply)
        multiply_button.grid(row=0, column=2, padx=2, pady=2)

        divide_button = Button(btn_frame, text="÷", width=4, command=self.divide)
        divide_button.grid(row=0, column=3, padx=2, pady=2)

        power_button = Button(btn_frame, text="x^y", width=4, command=self.power)
        power_button.grid(row=1, column=0, padx=2, pady=(8, 0))
        
        sqrt_button = Button(btn_frame, text="√", width=4, command=self.square_root)
        sqrt_button.grid(row=1, column=1, padx=2, pady=(8, 0))

        destroy_button = Button(btn_frame, text="Close", command=self.win.destroy)
        destroy_button.grid(row=1, column=2, columnspan=2, sticky="we", pady=(8, 0))

    def add(self):
        self.result.set(f"Result: {self.n1.get() + self.n2.get()}")

    def subtract(self):
        self.result.set(f"Result: {self.n1.get() - self.n2.get()}")

    def multiply(self):
        self.result.set(f"Result: {self.n1.get() * self.n2.get()}")

    def divide(self):
        n1, n2 = self.n1.get(), self.n2.get()
        if n2 == 0:
            self.result.set("Result: error (÷0)")
            return
        self.result.set(f"Result: {n1 / n2}")
    
    def power(self):
        self.result.set(f"Result: {self.n1.get() ** self.n2.get()}")
    
    def square_root(self):
        n1 = self.n1.get()
        if n1 < 0:
            self.result.set("Result: error (√-1)")
            return
        self.result.set(f"Result: {n1 ** 0.5}")

def main():
    Calculator().run()
main()