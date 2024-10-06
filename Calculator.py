import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка: деление на 0")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, insertwidth=4, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_value = 1
col_value = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=clear).grid(row=row_value, column=col_value)
    elif button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=calculate).grid(row=row_value, column=col_value)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: button_click(b)).grid(row=row_value, column=col_value)
    
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

root.mainloop()