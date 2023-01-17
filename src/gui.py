from cmath import exp
from tkinter import Label, ttk 
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import guicontroller as gc


FROM_X = -50
TO_X = 50
SPIN_WIDTH = 10
PADY_BOXES = (0, 5)
BUTTON_PAD = 3
BUTTON_WIDTH = 8


def run():
    root = ThemedTk(theme="adapta")
    root.title("Sistema de Equações Lineares")
    root.geometry('1000x630+250+100')
    root.resizable(False, False) 

    input_frame = ttk.LabelFrame(root, text="Entrada", padding=20)
    output_frame = ttk.LabelFrame(root, text="Saída", padding=20)

    button_frame = ttk.Frame(input_frame, padding=20)


    numofeqn_label = ttk.Label(input_frame, text="Número de equações")
    numofeqn_var = tk.IntVar()
    numofeqn_var.set(3)
    numofeqn_spin = ttk.Spinbox(input_frame, textvariable=numofeqn_var, width=SPIN_WIDTH, from_=0, to=TO_X)


    enter_label= ttk.Label(input_frame, text="Entrar equação", width=20)
    entry_string = tk.StringVar()
    exp_entry = ttk.Entry(input_frame, textvariable=entry_string, width=40, state="disabled")
    entry_string.trace_add("write", lambda *args: gc.string_entered(exp_entry))
    file_btn = ttk.Button(input_frame, text="Escolher arquivo", command=lambda:gc.choose_file(output_txt))

    calc_btn = ttk.Button(input_frame, text="Calcular", command=lambda: gc.calc(output_txt, method.get()))

    confirm_btn = ttk.Button(input_frame, text="Confirmar", width=BUTTON_WIDTH + 2, command=lambda *args: gc.confirm(output_txt, numofeqn_var.get(), reset_btn, enter_btn, exp_entry))
    reset_btn = ttk.Button(input_frame, text="Reset", state="disabled", width=BUTTON_WIDTH, command=lambda *args: gc.reset(output_txt, reset_btn, enter_btn, exp_entry))
    enter_btn = ttk.Button(input_frame, text="Entrar", state="disabled", width=BUTTON_WIDTH, command=lambda *args: gc.enter_eqn(output_txt, exp_entry.get(), enter_btn, exp_entry))


    methods = [
        "Todos",
        "Gauss Jordan",
        "Eliminação Gaussiana",
        "Decomposição LU",
        "Gauss siedel"
    ]
    method = tk.StringVar()
    method.set(methods[0])
    method_label = ttk.Label(input_frame, text="Método")
    method_options = ttk.Combobox(input_frame, textvariable=method, values=methods, state="readonly")
    method_options.config(width=20)

    var_widgets = [
    ]


    method.trace_add("write", lambda *args: gc.method_change(var_widgets, method.get(), methods, output_txt, reset_btn, enter_btn, exp_entry))
    
    output_txt = tk.Text(output_frame, width=40, state="disabled", height=30, wrap=tk.NONE)
    scrollbar_y = ttk.Scrollbar(output_frame, orient='vertical', command=output_txt.yview)
    scrollbar_x = ttk.Scrollbar(output_frame, orient='horizontal', command=output_txt.xview)
    output_txt.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

    
    clear_btn = ttk.Button(button_frame, text="limpar", width=BUTTON_WIDTH, command=lambda *args: gc.clear(exp_entry))
    plus_button = ttk.Button(button_frame, text="+", width=BUTTON_WIDTH, command=lambda *args: gc.plus(exp_entry))
    minus_button = ttk.Button(button_frame, text="-", width=BUTTON_WIDTH, command=lambda *args: gc.minus(exp_entry))
    mult_button = ttk.Button(button_frame, text="*", width=BUTTON_WIDTH, command=lambda *args: gc.mult(exp_entry))
    div_button = ttk.Button(button_frame, text="/", width=BUTTON_WIDTH, command=lambda *args: gc.div(exp_entry))
    pwr_button = ttk.Button(button_frame, text="^", width=BUTTON_WIDTH, command=lambda *args: gc.pwr(exp_entry))
    sqrt_button = ttk.Button(button_frame, text="sqrt()", width=BUTTON_WIDTH, command=lambda *args: gc.sqrt(exp_entry))
    leftbracket_button = ttk.Button(button_frame, text="(", width=BUTTON_WIDTH, command=lambda *args: gc.leftbracket(exp_entry))
    rightbracket_button = ttk.Button(button_frame, text=")", width=BUTTON_WIDTH, command=lambda *args: gc.rightbracket(exp_entry))
    cos_button = ttk.Button(button_frame, text="cos()", width=BUTTON_WIDTH, command=lambda *args: gc.cos(exp_entry))
    sin_button = ttk.Button(button_frame, text="sin()", width=BUTTON_WIDTH, command=lambda *args: gc.sin(exp_entry))
    e_button = ttk.Button(button_frame, text="E", width=BUTTON_WIDTH, command=lambda *args: gc.e(exp_entry))
    x_button = ttk.Button(button_frame, text="x", width=BUTTON_WIDTH, command=lambda *args: gc.x(exp_entry))


    input_frame.grid(column=0, row=0, padx=20, pady=20)
    output_frame.grid(column=1, row=0, padx=20, pady=20. , sticky=tk.N+tk.S+tk.W)

    button_frame.grid(column=3, row=2, rowspan=10)

    method_label.grid(column=0, row=0, sticky=tk.W)
    method_options.grid(column=0, row=1, columnspan = 2, sticky=tk.W, pady=PADY_BOXES)
    file_btn.grid(column=3, row=1)

    numofeqn_label.grid(column=0, row=2, sticky=tk.W)
    numofeqn_spin.grid(column=0, row=3, sticky=tk.W, pady=PADY_BOXES)
    confirm_btn.grid(column=1, row=3,sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)
    reset_btn.grid(column=2, row=3, sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)

    enter_label.grid(column=0, row=4, sticky=tk.W)
    exp_entry.grid(column=0, row=5, columnspan=2, sticky=tk.W, pady=PADY_BOXES)
    enter_btn.grid(column=2, row=5, sticky=tk.W, padx=BUTTON_PAD, pady=BUTTON_PAD)

    calc_btn.grid(column=3, row=12, padx=10, pady=10)

    clear_btn.grid(column=0, row=0, columnspan=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    plus_button.grid(column=0, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    minus_button.grid(column=1, row=1, padx=BUTTON_PAD, pady=BUTTON_PAD)
    mult_button.grid(column=0, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    div_button .grid(column=1, row=2, padx=BUTTON_PAD, pady=BUTTON_PAD)
    pwr_button.grid(column=0, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    sqrt_button.grid(column=1, row=3, padx=BUTTON_PAD, pady=BUTTON_PAD)
    leftbracket_button.grid(column=0, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)
    rightbracket_button.grid(column=1, row=4, padx=BUTTON_PAD, pady=BUTTON_PAD)
    cos_button.grid(column=0, row=5, padx=BUTTON_PAD, pady=BUTTON_PAD)
    sin_button.grid(column=1, row=5, padx=BUTTON_PAD, pady=BUTTON_PAD)
    e_button.grid(column=0, row=6, padx=BUTTON_PAD, pady=BUTTON_PAD)
    x_button.grid(column=1, row=6, padx=BUTTON_PAD, pady=BUTTON_PAD)


    output_txt.grid(column=0, row=0)
    scrollbar_y.grid(column=1, row=0, sticky=tk.N+tk.S)
    scrollbar_x.grid(column=0, row=1, columnspan=2, sticky=tk.W+tk.E)

    root.protocol("WM_DELETE_WINDOW", lambda:gc.destroyer(root))
    root.mainloop()

run()