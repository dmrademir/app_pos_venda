import ttkbootstrap as ttk
from tkinter import Frame, Label, LabelFrame
from ttkbootstrap.constants import *

# Criando a aplicação principal
root = ttk.Window(themename="darkly")
root.title("Área de Testes")
root.geometry("1020x700")
root.position_center()




# # Linha 1
# ttk.Label(root, text="coluna 1").grid(row=0, column=0, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=22, font=("Arial", 16))
# entry_cliente.grid(row=1, column=0, columnspan=2 ,padx=5, pady=5, sticky="w")

# # ttk.Label(root, text="coluna 2").grid(row=0, column=1, padx=5, pady=3, sticky="w")
# # entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# # entry_cliente.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 3").grid(row=0, column=2, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=1, column=2, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 4").grid(row=0, column=3, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=1, column=3, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 5").grid(row=0, column=4, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=1, column=4, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 5").grid(row=0, column=4, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=1, column=4, padx=5, pady=5, sticky="w")


# # Linha 2
# ttk.Label(root, text="coluna 1").grid(row=2, column=0, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=3, column=0, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 2").grid(row=2, column=1, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 3").grid(row=2, column=2, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=3, column=2, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 4").grid(row=2, column=3, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=3, column=3, padx=5, pady=5, sticky="w")

# ttk.Label(root, text="coluna 5").grid(row=2, column=4, padx=5, pady=3, sticky="w")
# entry_cliente = ttk.Entry(root, width=10, font=("Arial", 16))
# entry_cliente.grid(row=3, column=4, padx=5, pady=5, sticky="w")


# Linha 3

b1 =  ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b1.pack(side=LEFT, padx=50, pady=10)

b1 =  ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b1.pack(side=RIGHT, padx=60, pady=10)

rb1 = ttk.Radiobutton(root, text="Não USAR", bootstyle="danger-toolbutton",value=1)
rb1.pack(side=LEFT, padx=50, pady=20)

rb2 = ttk.Radiobutton(root, text="Não USAR", bootstyle="toolbutton",value=1)
rb2.pack(side=LEFT, padx=50, pady=20)
rb2.configure(state="disabled")

# Iniciando o loop principal
root.mainloop()
