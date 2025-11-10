import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from cliente_frame import FrameCliente
from compra_frame import FrameCompra
from contato_frame import FrameContato

class AtendimentoFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # HEAD - Botões de ação
        self.botao_novo = ttk.Button(self, text="Novo Atendimento")
        self.botao_novo.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.botao_consulta = ttk.Button(self, text="Consulta")
        self.botao_consulta.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.botao_gravar = ttk.Button(self, text="Gravar")
        self.botao_gravar.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        # BODY - LabelFrames
        self.frame_cliente = self.frame_cliente = FrameCliente(self)
        self.frame_cliente.grid(row=1, column=0, columnspan=14, padx=5, pady=5, sticky="nsew")

        self.frame_compra = self.frame_compra = FrameCompra(self)
        self.frame_compra.grid(row=2, column=0, columnspan=14, padx=5, pady=5, sticky="nsew")

        # Frame Dados do Contato (ao lado do frame_cliente)
        self.frame_contato = FrameContato(self)
        self.frame_contato.grid(row=1, column=16, columnspan=13, rowspan=2, padx=5, pady=5, sticky="nsew")

