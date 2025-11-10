import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import scrolledtext

class FrameContato(ttk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master, text="Dados do Contato")

        # linha 0
        ttk.Label(self, text="contato com").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(self, width=10).grid(row=1, column=0, padx=5, pady=2, sticky="we")

        ttk.Label(self, text="telefone principal").grid(row=0, column=2, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=1, column=2, padx=5, pady=2, sticky="we")

        # linha 2
        ttk.Label(self, text="e-mail cnpj").grid(row=2, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=3, column=0, padx=5, pady=2, sticky="we")

        ttk.Label(self, text="e-mail cobrança").grid(row=2, column=1, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=3, column=1, padx=5, pady=2, sticky="we")

        # linha 4
        ttk.Label(self, text="telefone 1").grid(row=4, column=0, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=5, column=0, padx=5, pady=2, sticky="we")

        ttk.Label(self, text="telefone 2").grid(row=4, column=1, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=5, column=1, padx=5, pady=2, sticky="we")

        ttk.Label(self, text="telefone 3").grid(row=4, column=2, sticky="w", padx=5, pady=2)
        ttk.Entry(self).grid(row=5, column=2, padx=5, pady=2, sticky="we")

        # linha 6 – conseguiu contato
        self.chk_contato = ttk.Checkbutton(self, text="conseguiu contato?")
        self.chk_contato.grid(row=6, column=0, padx=5, pady=2, sticky="w")
        ttk.Combobox(self, values=["sim", "não"]).grid(row=6, column=1, padx=5, pady=2, sticky="we")
        ttk.Label(self, text="recebeu boleto?").grid(row=6, column=2, sticky="w", padx=5)
        ttk.Combobox(self).grid(row=6, column=3, padx=5, pady=2, sticky="we")

        # linha 7 – reclamação
        self.chk_reclamacao = ttk.Checkbutton(self, text="reclamação?")
        self.chk_reclamacao.grid(row=7, column=0, padx=5, pady=2, sticky="w")
        ttk.Combobox(self).grid(row=7, column=1, padx=5, pady=2, sticky="we")
        ttk.Label(self, text="nível de criticidade").grid(row=7, column=2, sticky="w", padx=5)
        ttk.Combobox(self).grid(row=7, column=3, padx=5, pady=2, sticky="we")

        # linha 8 – ocorrência
        self.chk_ocorrencia = ttk.Checkbutton(self, text="gerou ocorrência?")
        self.chk_ocorrencia.grid(row=8, column=0, padx=5, pady=2, sticky="w")
        ttk.Combobox(self).grid(row=8, column=1, padx=5, pady=2, sticky="we")
        ttk.Label(self, text="temperamento").grid(row=8, column=2, sticky="w", padx=5)
        ttk.Combobox(self).grid(row=8, column=3, padx=5, pady=2, sticky="we")

        # linha 9 – elogio
        self.chk_elogio = ttk.Checkbutton(self, text="houve elogio?")
        self.chk_elogio.grid(row=9, column=0, padx=5, pady=2, sticky="w")
        ttk.Combobox(self).grid(row=9, column=1, padx=5, pady=2, sticky="we")
        ttk.Label(self, text="nota de 0 a 10 (NPS)").grid(row=9, column=2, sticky="w", padx=5)
        ttk.Combobox(self, values=[str(i) for i in range(11)]).grid(row=9, column=3, padx=5, pady=2, sticky="we")

        # linha 12 – houve sugestão
        self.chk_contato_final = ttk.Checkbutton(self, text="houve sugestão?")
        self.chk_contato_final.grid(row=12, column=0, sticky="w", padx=5, pady=2)
        self.txt_contato_final = scrolledtext.ScrolledText(self, width=40, height=5)
        self.txt_contato_final.grid(row=13, column=0, padx=5, pady=2)
       
       
        ttk.Label(self, text="resumo da conversa:").grid(row=12, column=2, sticky="w", padx=5)
        self.txt_resumo = scrolledtext.ScrolledText(self, width=40, height=5)
        self.txt_resumo.grid(row=13, column=2, padx=5, pady=2)

        # espaçamento
        for i in range(15):
            self.rowconfigure(i, weight=1)
        for i in range(5):
            self.columnconfigure(i, weight=1)
