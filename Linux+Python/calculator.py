
import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

expression = ""

text_input = tk.Label(root, text="", font=("Arial", 16))
text_input.pack(pady=10)

text_result = tk.Label(root, text="Результат: ", font=("Arial", 14))
text_result.pack(pady=5)


def add_symbol(symbol):
    global expression
    expression += str(symbol)
    text_input.config(text=expression)


def clear():
    global expression
    expression = ""
    text_input.config(text="")
    text_result.config(text="Результат: ")


def calculate(operation):
    global expression
    try:
        parts = expression.split(operation)
        if len(parts) != 2:
            text_result.config(text="Введите два числа")
            return None

        a = float(parts[0])
        b = float(parts[1])

        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            if b == 0:
                text_result.config(text="На ноль делить нельзя")
                return None
            return a / b
    except ValueError:
        text_result.config(text="Ошибка ввода")
        return None


def multiple():
    add_symbol("*")


def divide():
    add_symbol("/")


def summy():
    add_symbol("+")


def diff():
    add_symbol("-")


def result():
    value = None

    for operation in ["+", "-", "*", "/"]:
        if operation in expression:
            value = calculate(operation)
            break

    if value is not None:
        text_result.config(text=f"Результат: {value}")


operations = [
    ("+", summy),
    ("-", diff),
    ("*", multiple),
    ("/", divide),
    ("=", result)
]

numbers_frame = tk.Frame(root)
numbers_frame.pack()

for number in range(10):
    button = tk.Button(
        numbers_frame,
        text=str(number),
        width=5,
        command=lambda n=number: add_symbol(n)
    )
    button.grid(row=number // 3, column=number % 3, padx=3, pady=3)

operations_frame = tk.Frame(root)
operations_frame.pack(pady=10)

for i, (text, function) in enumerate(operations):
    button = tk.Button(
        operations_frame,
        text=text,
        width=5,
        command=function
    )
    button.grid(row=i // 3, column=i % 3, padx=3, pady=3)

clear_button = tk.Button(root, text="Очистить", command=clear)
clear_button.pack(pady=5)

root.mainloop()
