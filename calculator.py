import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Set the minimum size of the window
        self.root.minsize(300, 400)

        self.current_input = ""
        self.operation = ""
        self.previous_input = ""

        # Entry widget to display the equation
        self.result_var = tk.StringVar()
        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), justify='right', bd=10)
        self.result_entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Configure grid to make buttons symmetric
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)

        # Buttons layout
        buttons = [
           ('C', 1, 0), ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), 
            ('/', 2, 0), ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 3, 0),
            ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 4, 0),
            ('0', 4, 2), ('=', 4, 3), ('+', 4, 1)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, width=5, height=2, font=('Arial', 18), command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.clear()
        elif char == '=':
            self.calculate()
        else:
            self.append_to_input(char)

    def append_to_input(self, char):
        if char in "+-*/":
            # Save the current operation
            if self.current_input:
                if self.previous_input:  # If there's already a previous input, calculate it first
                    self.calculate()
                self.operation = char
                self.previous_input = self.current_input
                self.current_input = ''
        else:
            self.current_input += str(char)

        self.update_display()

    def calculate(self):
        if self.current_input == '' or self.previous_input == '':
            return

        prev = float(self.previous_input)
        curr = float(self.current_input)
        result = 0

        if self.operation == '+':
            result = prev + curr
        elif self.operation == '-':
            result = prev - curr
        elif self.operation == '*':
            result = prev * curr
        elif self.operation == '/':
            if curr == 0:
                result = "Error"
            else:
                result = prev / curr

        self.current_input = str(result)
        self.previous_input = ''
        self.operation = ''
        self.update_display()

    def clear(self):
        self.current_input = ''
        self.previous_input = ''
        self.operation = ''
        self.update_display()

    def update_display(self):
        display = f"{self.previous_input} {self.operation} {self.current_input}".strip()
        self.result_var.set(display)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
