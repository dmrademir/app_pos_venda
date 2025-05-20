import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

class FrameCompra(ttk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master, text="Compra")

        # Linha 0
        ttk.Label(self, text="representante").grid(row=0, column=0, sticky="w", padx=2, pady=2)
        self.entry_representante = ttk.Entry(self, width=25)
        self.entry_representante.grid(row=1, column=0, columnspan=3, sticky="ew", padx=2)

        ttk.Label(self, text="nota fiscal").grid(row=0, column=4, sticky="w", padx=2, pady=2)
        self.entry_nota_fiscal = ttk.Entry(self, width=25)
        self.entry_nota_fiscal.grid(row=1, column=4, columnspan=3, sticky="ew", padx=2)

        # Linha 1
        ttk.Label(self, text="tipo de compra").grid(row=2, column=0, sticky="w", padx=2, pady=2)
        self.entry_tipo_compra = ttk.Entry(self, width=25)
        self.entry_tipo_compra.grid(row=3, column=0, columnspan=2, sticky="ew", padx=2)

        ttk.Label(self, text="pedido ruvolo").grid(row=2, column=3, sticky="w", padx=2, pady=2)
        self.entry_pedido_ruvolo = ttk.Entry(self, width=25)
        self.entry_pedido_ruvolo.grid(row=3, column=3, columnspan=2, sticky="ew", padx=2)

        ttk.Label(self, text="pedido bees").grid(row=2, column=6, sticky="w", padx=2, pady=2)
        self.entry_pedido_bees = ttk.Entry(self, width=25)
        self.entry_pedido_bees.grid(row=3, column=6, columnspan=2, sticky="ew", padx=2)

        # Linha 2
        ttk.Label(self, text="data do pedido").grid(row=4, column=0, sticky="w", padx=2, pady=2)
        self.entry_data_pedido = ttk.Entry(self, width=20)
        self.entry_data_pedido.grid(row=5, column=0, sticky="ew", padx=2)

        ttk.Label(self, text="data de saída").grid(row=4, column=2, sticky="w", padx=2, pady=2)
        self.entry_data_saida = ttk.Entry(self, width=20)
        self.entry_data_saida.grid(row=5, column=2, sticky="ew", padx=2)

        ttk.Label(self, text="valor c/imposto").grid(row=4, column=4, sticky="w", padx=2, pady=2)
        self.entry_valor_com_imposto = ttk.Entry(self, width=20)
        self.entry_valor_com_imposto.grid(row=5, column=4, sticky="ew", padx=2)

        ttk.Label(self, text="valor s/imposto").grid(row=4, column=6, sticky="w", padx=2, pady=2)
        self.entry_valor_sem_imposto = ttk.Entry(self, width=20)
        self.entry_valor_sem_imposto.grid(row=5, column=6, sticky="ew", padx=2)

        # Linha 3
        ttk.Label(self, text="cód. transportadora").grid(row=6, column=0, sticky="w", padx=2, pady=2)
        self.entry_cod_transportadora = ttk.Entry(self, width=25)
        self.entry_cod_transportadora.grid(row=7, column=0, columnspan=2, sticky="ew", padx=2)

        ttk.Label(self, text="transportadora").grid(row=6, column=3, sticky="w", padx=2, pady=2)
        self.entry_transportadora = ttk.Entry(self, width=25)
        self.entry_transportadora.grid(row=7, column=3, columnspan=2, sticky="ew", padx=2)

        ttk.Label(self, text="frete").grid(row=6, column=6, sticky="w", padx=2, pady=2)
        self.entry_frete = ttk.Entry(self, width=25)
        self.entry_frete.grid(row=7, column=6, sticky="ew", padx=2)

        # Linha 4
        ttk.Label(self, text="cnpj transportadora").grid(row=8, column=0, sticky="w", padx=2, pady=2)
        self.entry_cnpj_transportadora = ttk.Entry(self, width=30)
        self.entry_cnpj_transportadora.grid(row=9, column=0, columnspan=3, sticky="ew", padx=2)

        # Configura espaçamento
        for i in range(10):
            self.rowconfigure(i, weight=1)
        for i in range(10):
            self.columnconfigure(i, weight=1)
