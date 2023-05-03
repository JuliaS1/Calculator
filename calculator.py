import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        master.geometry('400x400')

        # Create the Entry widget for display
        self.display = tk.Entry(self.master, width=30, font=("Arial", 12), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for each digit and operation
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)

        # Bind the keyboard to the Entry widget
        self.master.bind("<Key>", self.key_press)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=10, height=4, font=("Arial", 12),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, text)

    def key_press(self, event):
        if event.char.isdigit() or event.char in [".", "/", "*", "-", "+"]:
            self.display.insert(tk.END, event.char)
        elif event.keysym == "Return":
            self.button_click("=")
        elif event.keysym == "BackSpace":
            self.display.delete(len(self.display.get())-1, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
