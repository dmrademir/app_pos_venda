import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FrameCliente(ttk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master, text="Cliente")

        # linha 0
        self.label_nome = ttk.Label(self, text="nome")
        self.label_nome.grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.entry_nome = ttk.Entry(self, width=80)
        self.entry_nome.grid(row=1, column=0, columnspan=6, sticky="we", padx=5, pady=2)

        # linha 2
        self.label_codigo = ttk.Label(self, text="código")
        self.label_codigo.grid(row=2, column=0, sticky="w", padx=5, pady=2)
        self.entry_codigo = ttk.Entry(self, width=20)
        self.entry_codigo.grid(row=3, column=0, sticky="we", padx=5, pady=2)

        self.label_cnpj = ttk.Label(self, text="cnpj")
        self.label_cnpj.grid(row=2, column=1, sticky="w", padx=5, pady=2)
        self.entry_cnpj = ttk.Entry(self, width=25)
        self.entry_cnpj.grid(row=3, column=1, sticky="we", padx=5, pady=2)

        # linha 4
        self.label_endereco = ttk.Label(self, text="endereço")
        self.label_endereco.grid(row=4, column=0, sticky="w", padx=5, pady=2)
        self.entry_endereco = ttk.Entry(self, width=80)
        self.entry_endereco.grid(row=5, column=0, columnspan=6, sticky="we", padx=5, pady=2)

        # linha 6
        self.label_numero = ttk.Label(self, text="número")
        self.label_numero.grid(row=6, column=0, sticky="w", padx=5, pady=2)
        self.entry_numero = ttk.Entry(self, width=10)
        self.entry_numero.grid(row=7, column=0, sticky="we", padx=5, pady=2)

        self.label_bairro = ttk.Label(self, text="bairro")
        self.label_bairro.grid(row=6, column=2, sticky="w", padx=5, pady=2)
        self.entry_bairro = ttk.Entry(self, width=25)
        self.entry_bairro.grid(row=7, column=2, sticky="we", padx=5, pady=2)

        # linha 8
        self.label_cidade = ttk.Label(self, text="cidade")
        self.label_cidade.grid(row=8, column=0, sticky="w", padx=5, pady=2)
        self.entry_cidade = ttk.Entry(self, width=30)
        self.entry_cidade.grid(row=9, column=0, sticky="we", padx=5, pady=2)

        self.label_cep = ttk.Label(self, text="cep")
        self.label_cep.grid(row=8, column=1, sticky="w", padx=5, pady=2)
        self.entry_cep = ttk.Entry(self, width=15)
        self.entry_cep.grid(row=9, column=1, sticky="we", padx=5, pady=2)

        self.label_uf = ttk.Label(self, text="uf")
        self.label_uf.grid(row=8, column=2, sticky="w", padx=5, pady=2)
        self.entry_uf = ttk.Entry(self, width=10)
        self.entry_uf.grid(row=9, column=2, sticky="we", padx=5, pady=2)

        # Configura espaçamento igual ao compra_frame
        for i in range(10):
            self.rowconfigure(i, weight=1)
        for i in range(10):
            self.columnconfigure(i, weight=1)
