import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import math

root = tk.Tk()
root.title("Квадратные уравнения")
root.geometry("700x600")
title_frame = tk.Frame(root, bg="#b3d9ff")
title_frame.pack(fill=tk.X, pady=5)
title_label = tk.Label(
    title_frame, 
    text="Решение квадратного уравнения", 
    font=("Arial", 16), 
    bg="#b3d9ff", 
    padx=10, 
    pady=10
)
title_label.pack(fill=tk.X)
eq_frame = tk.Frame(root)
eq_frame.pack(fill=tk.X, pady=10)


a_label = tk.Label(eq_frame, text="", width=2)
a_label.grid(row=0, column=0)
a_entry = tk.Entry(eq_frame, width=5, bg="lightblue")
a_entry.insert(0, "2")
a_entry.grid(row=0, column=1, padx=5)
x2_label = tk.Label(eq_frame, text="x²+")
x2_label.grid(row=0, column=2)
b_entry = tk.Entry(eq_frame, width=5, bg="lightblue")
b_entry.insert(0, "-10")
b_entry.grid(row=0, column=3, padx=5)
x_label = tk.Label(eq_frame, text="x+")
x_label.grid(row=0, column=4)
c_entry = tk.Entry(eq_frame, width=5, bg="lightblue")
c_entry.insert(0, "1")
c_entry.grid(row=0, column=5, padx=5)
eq_label = tk.Label(eq_frame, text="=0")
eq_label.grid(row=0, column=6)


result_frame = tk.Frame(root)
result_frame.pack(fill=tk.X, pady=10)
result_label = tk.Label(
    result_frame, 
    text="", 
    bg="yellow", 
    font=("Arial", 12), 
    width=40, 
    height=3
)
result_label.pack(pady=10)
graph_frame = tk.Frame(root)
graph_frame.pack(fill=tk.BOTH, expand=True, pady=10)


def solve_equation():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        d = b**2 - 4*a*c
        
        result_text = f"D={d:.1f}\n"
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            result_text += f"X1={x1:.1f}\nX2={x2:.1f}"
        elif d == 0:
            x = -b / (2*a)
            result_text += f"X={x:.1f}"
        else:
            result_text += "Нет действительных корней"
        result_label.config(text=result_text)
        
    except ValueError:
        result_label.config(text="Ошибка! Введите числовые значения.")
    except ZeroDivisionError:
        result_label.config(text="Ошибка! Коэффициент a не может быть равен 0.")


def plot_graph():
    try:
        for widget in graph_frame.winfo_children():
            widget.destroy()
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())
        fig = plt.Figure(figsize=(5, 4))
        ax = fig.add_subplot(111)
        x = np.linspace(-10, 10, 100)
        y = a * x**2 + b * x + c
        ax.plot(x, y, 'bo-', markersize=4)
        ax.grid(True)
        ax.set_title("Квадратное уравнение")
        ax.set_xlabel("x")
        ax.set_ylabel("y") 
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
    except ValueError:
        error_label = tk.Label(graph_frame, text="Ошибка! Введите числовые значения.")
        error_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, pady=5)
solve_button = tk.Button(
    button_frame, 
    text="Решить", 
    command=solve_equation, 
    bg="green", 
    fg="white", 
    width=10,
    height=2
)
solve_button.pack(side=tk.LEFT, padx=20)

graph_button = tk.Button(
    button_frame, 
    text="График", 
    command=plot_graph, 
    bg="blue", 
    fg="white", 
    width=10,
    height=2
)
graph_button.pack(side=tk.LEFT, padx=20)
solve_equation()
root.mainloop()