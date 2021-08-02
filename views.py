# Este trabajo es de Guido Ignacio Goroisto Parodi, guidoparodi.dv@gmail.com, comocido tambien como, Eloy Gorosito Parodi
import tkinter as tk
from tkinter import ttk
from model import mysql_scrip


master = tk.Tk()
bg_master = "#57FACE"  # fefefe
master.configure(bg=bg_master)
master.title("Base de Datos")
master.resizable(1, 1)


# Variables de emtrada
# Entradas
db_host = tk.StringVar()
db_name = tk.StringVar()
db_pass = tk.StringVar()
db_database = tk.StringVar()
db_table = tk.StringVar()
# Variables esteticas

bg_label = "#9897F5"
fg_label = "white"
bg_entrya = bg_master  # "#85A0F5"
fg_entrya = "black"
bg_entryb = "#94D1FA"
fg_entryb = "white"
bg_ok = "Green"
bg_warning = "Yellow"
bg_no = "Orange"
bg_btn = "#9897F5"
###### Contenido ######

lb_host = tk.Label(
    master,
    bg=bg_label,
    fg=fg_label,
    text="   HOST:   ",
    justify="center",
) 
imp_host = tk.Entry(
    master,
    bg=bg_entrya,
    fg=fg_entrya,
    bd="5",
    relief="groove",
    justify="center",
    textvariable=db_host,
    width=35,
)
lb_name = tk.Label(
    master,
    bg=bg_label,
    fg=fg_label,
    text="name:",
    justify="center",
)
imp_name = tk.Entry(
    master,
    bg=bg_entrya,
    fg=fg_entrya,
    bd="5",
    relief="groove",
    justify="center",
    textvariable=db_name,
    width=35,
)
lb_pass = tk.Label(
    master,
    bg=bg_label,
    fg=fg_label,
    text="pass:",
    justify="center",
)
imp_pass = tk.Entry(
    master,
    bg=bg_entrya,
    fg=fg_entrya,
    bd="5",
    relief="groove",
    justify="center",
    textvariable=db_pass,
    width=35,
)
lb_database = tk.Label(
    master,
    bg=bg_label,
    fg=fg_label,
    text="Data Base:",
    justify="center",
)
imp_database = tk.Entry(
    master,
    bg=bg_entrya,
    fg=fg_entrya,
    bd="5",
    relief="groove",
    justify="center",
    textvariable=db_database,
    width=35,
)
lb_table = tk.Label(
    master,
    bg=bg_label,
    fg=fg_label,
    text="Table:",
    justify="center",
)
imp_table = tk.Entry(
    master,
    bg=bg_entrya,
    fg=fg_entrya,
    bd="5",
    relief="groove",
    justify="center",
    textvariable=db_table,
    width=35,
)


def checkdb():

    if not db_host.get():
        print("Por favor Ingrese el HOST de la base de datos")
    elif not db_name.get():
        print("Por favor Ingrese el USUARIO de la base de datos")
    elif not db_database.get():
        print("Por favor Ingrese el NOMBRE de la base de datos")
    elif not db_table.get():
        print("Por favor Ingrese el NOMBRE DE TABLA de la base de datos")
    else:
        respuesta.grid(row=2, column=0)
        if not db_pass.get():
            # Modelo
            DataBase = mysql_scrip(
                db_host.get(),
                db_name.get(),
                db_database.get(),
                db_table.get(),
            )
        else:
            # Modelo
            DataBase = mysql_scrip(
                db_host.get(),
                db_name.get(),
                db_pass.get(),
                db_database.get(),
                db_table.get(),
            )
        print("todo bien hasta aca")
        estado = DataBase.show_table()
        if estado:
            respuesta.configure(text="Conectado", bg=bg_ok)
        else:
            respuesta.configure(text="Desconectado", bg=bg_no)
        respuesta.grid(row=2, column=0)


btn_check = tk.Button(
    master,
    text="CHECK",
    command=checkdb,
    bg=bg_btn,
    width=35,
)
btn_alta = tk.Button(
    master,
    text="ALTA",
    command=None,
    bg=bg_btn,
    width=35,
)
btn_baja = tk.Button(
    master,
    text="MODIFICACION",
    command=None,
    bg=bg_btn,
    width=35,
)
btn_modi = tk.Button(
    master,
    text="DELETE",
    command=None,
    bg=bg_btn,
    width=35,
)
respuesta = tk.Label(master, text="Check Conexion.", bg=bg_warning)


tree_tabla = ttk.Treeview(
    master, height=12, column=(1, 2, 3, 4, 5), show="headings", selectmode="browse"
)

# tree_tabla.pack(side=LEFT, anchor=W, expand=YES, fill=BOTH)
tree_tabla.heading(1, text="ID")
tree_tabla.heading(2, text="Nombre")
tree_tabla.heading(3, text="Apellido")
tree_tabla.heading(4, text="Email")
tree_tabla.heading(5, text="Descripción")
tree_tabla.column(1, width=80, minwidth=30, stretch="YES")
tree_tabla.column(2, width=206, minwidth=30, stretch="YES")
tree_tabla.column(3, width=206, minwidth=30, stretch="YES")
tree_tabla.column(4, width=206, minwidth=30, stretch="YES")
tree_tabla.column(5, width=206, minwidth=35, stretch="YES")
# Barra de desplazamiento vertical Tkk Scrollbar
barra_tree = ttk.Scrollbar(master, orient="vertical", command=tree_tabla.yview)
# barra_tree.pack(side=RIGHT, expand=YES, fill=BOTH)
tree_tabla.configure(yscrollcommand=barra_tree.set)


lb_host.grid(row=0, column=0, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
imp_host.grid(row=0, column=1, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
lb_name.grid(row=0, column=2, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
imp_name.grid(row=0, column=3, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
lb_pass.grid(row=0, column=4, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
imp_pass.grid(row=0, column=5, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
lb_database.grid(row=1, column=0, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
imp_database.grid(row=1, column=1, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
lb_table.grid(row=1, column=2, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
imp_table.grid(row=1, column=3, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSEW")
btn_check.grid(
    row=1, column=4, ipady=6, ipadx=6, padx=2, pady=2, columnspan=2, sticky="NSEW"
)
tree_tabla.grid(
    row=2, column=0, ipady=6, ipadx=6, padx=2, pady=2, columnspan=6, sticky="NSEW"
)
barra_tree.grid(row=2, column=5, ipady=6, ipadx=6, padx=2, pady=2, sticky="NSE")
btn_alta.grid(
    row=3, column=0, ipady=6, ipadx=6, padx=2, pady=2, columnspan=2, sticky="NSEW"
)
btn_baja.grid(
    row=3, column=2, ipady=6, ipadx=6, padx=2, pady=2, columnspan=2, sticky="NSEW"
)
btn_modi.grid(
    row=3, column=4, ipady=6, ipadx=6, padx=2, pady=2, columnspan=2, sticky="NSEW"
)

"""
# Entradas de texto
lb_input1 = tk.Label(
    master,
    bg=bg_label,
    fg="white",
    text="Nombre:",
    justify="center",
)
nombre = tk.StringVar()
input1 = tk.Entry(
    master,
    bg=bg_entryb,
    fg="black",
    bd="5",
    relief="groove",
    justify="center",
    textvariable=nombre,
)
lb_input2 = tk.Label(
    master,
    bg=bg_label,
    fg="white",
    text="apellido:",
    justify="center",
)
apellido = tk.StringVar()
input2 = tk.Entry(
    master,
    bg="#94D1FA",
    fg="black",
    bd="5",
    relief="groove",
    justify="center",
    textvariable=apellido,
)
lb_input3 = tk.Label(
    master,
    bg=bg_label,
    fg="white",
    text="Email:",
    justify="center",
)
email = tk.StringVar()
input3 = tk.Entry(
    master,
    bg=bg_entryb,
    fg="black",
    bd="5",
    relief="groove",
    justify="center",
    textvariable=email,
)
lb_input1.grid(row=2, column=0, ipady=4, ipadx=2)
input1.grid(row=2, column=1, ipady=4, ipadx=2)
lb_input2.grid(row=2, column=2, ipady=4, ipadx=2)
input2.grid(row=2, column=3, ipady=4, ipadx=2)
lb_input3.grid(row=2, column=4, ipady=4, ipadx=2)
input3.grid(row=2, column=5, ipady=4, ipadx=2)

"""

master.mainloop()