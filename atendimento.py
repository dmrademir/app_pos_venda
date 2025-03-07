import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from database import conectar_bd

class AtendimentoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Formulário de Atendimento
        ttk.Label(self, text="cliente", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=3, sticky="w")
        self.entry_cliente = ttk.Entry(self, width=30, font=("Arial", 20))
        self.entry_cliente.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="data registro", font=("Arial", 10)).grid(row=0, column=1, padx=5, pady=3, sticky="w")
        self.entry_data_registro = ttk.Entry(self, width=10, font=("Arial", 20))
        self.entry_data_registro.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="cód. cliente", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=3, sticky="w")
        self.entry_cod_cliente = ttk.Entry(self, width=10, font=("Arial", 20))
        self.entry_cod_cliente.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="cnpj", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=3, sticky="w")
        self.entry_cnpj = ttk.Entry(self, width=40, font=("Arial", 16))
        self.entry_cnpj.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="cidade", font=("Arial", 10)).grid(row=2, column=1, padx=5, pady=3, sticky="w")
        self.entry_cidade = ttk.Entry(self, width=20, font=("Arial", 16))
        self.entry_cidade.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="uf", font=("Arial", 10)).grid(row=2, column=2, padx=5, pady=3, sticky="w")
        self.entry_uf = ttk.Entry(self, width=5, font=("Arial", 16))
        self.entry_uf.grid(row=3, column=2, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="e-mail", font=("Arial", 10)).grid(row=4, column=0, padx=5, pady=3, sticky="w")
        self.entry_email = ttk.Entry(self, width=40, font=("Arial", 16))
        self.entry_email.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="telefone do contato cnpj", font=("Arial", 10)).grid(row=4, column=1, padx=5, pady=3, sticky="w")
        self.entry_tel_cnpj = ttk.Entry(self, width=20, font=("Arial", 16))
        self.entry_tel_cnpj.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="tel de contato 1", font=("Arial", 10)).grid(row=4, column=2, padx=5, pady=3, sticky="w")
        self.entry_tel_1 = ttk.Entry(self, width=20, font=("Arial", 16))
        self.entry_tel_1.grid(row=5, column=2, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="contato com:", font=("Arial", 10)).grid(row=6, column=1, padx=5, pady=5, sticky="w")
        self.entry_contato_com = ttk.Entry(self, width=20, font=("Arial", 16))
        self.entry_contato_com.grid(row=7, column=1, columnspan=2,padx=5, pady=5, sticky="w")

        btn_adicionar = ttk.Button(self, text="Salvar Atendimento", bootstyle=SUCCESS, command=self.adicionar_atendimento)
        btn_adicionar.grid(row=8, column=0, columnspan=2, pady=10)

        # Tabela de Atendimentos
        self.tree = ttk.Treeview(self, columns=("ID", "Cliente", "Email", "Resumo"), show="headings")
        for col in ("ID", "Cliente", "Email", "Resumo"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=250)
        self.tree.grid(row=9, column=0, columnspan=3, pady=10)

        self.carregar_atendimentos()

    def carregar_atendimentos(self):
        """Carrega os atendimentos na tabela"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            conn = conectar_bd()
            if conn is None:
                return
            cur = conn.cursor()
            cur.execute("SELECT id, cliente, email, resumo_conversa FROM atendimento")
            for row in cur.fetchall():
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar atendimentos: {e}")
        finally:
            if conn:
                conn.close()

    def adicionar_atendimento(self):
        """Adiciona um novo atendimento ao banco de dados"""
        cliente = self.entry_cliente.get()
        email = self.entry_email.get()
        contato_com = self.entry_contato_com.get()
        
        if not cliente or not email or not contato_com:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return

        try:
            conn = conectar_bd()
            if conn is None:
                return
            cur = conn.cursor()
            cur.execute("INSERT INTO atendimento (cliente, email, resumo_conversa) VALUES (?, ?, ?)",
                        (cliente, email, contato_com))
            conn.commit()
            messagebox.showinfo("Sucesso", "Atendimento salvo com sucesso!")
            self.carregar_atendimentos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar atendimento: {e}")
        finally:
            if conn:
                conn.close()
