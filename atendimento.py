import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from database import conectar_bd

class AtendimentoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Formulário de Atendimento
        ttk.Label(self, text="nome", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=3, sticky="w")
        self.entry_nome = ttk.Entry(self, width=30, font=("Arial", 20) )
        self.entry_nome.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="registro", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=3, sticky="w")
        self.entry_registro = ttk.Entry(self, width=10, font=("Arial", 20) )
        self.entry_registro.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="cnpj", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=3, sticky="w")
        self.entry_cnpj = ttk.Entry(self, width=20, font=("Arial", 16) )
        self.entry_cnpj.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="cidade", font=("Arial", 10)).grid(row=2, column=1, padx=5, pady=3, sticky="w")
        self.entry_cidade = ttk.Entry(self, width=20, font=("Arial", 16) )
        self.entry_cidade.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(self, text="uf", font=("Arial", 10)).grid(row=2, column=2, padx=5, pady=3, sticky="e")
        self.entry_uf = ttk.Entry(self, width=5, font=("Arial", 16) )
        self.entry_uf.grid(row=3, column=2, padx=5, pady=5, sticky="e")
       

        ttk.Label(self, text="Descrição:", font=("Arial", 10)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_descricao = ttk.Text(self, height=5, width=40)
        self.entry_descricao.grid(row=5, column=0, padx=5, pady=5, sticky="w")

        btn_adicionar = ttk.Button(self, text="Salvar Atendimento", bootstyle=SUCCESS, command=self.adicionar_atendimento)
        btn_adicionar.grid(row=6, column=0, columnspan=2, pady=10)

        # Tabela de Atendimentos
        self.tree = ttk.Treeview(self, columns=("ID", "Nome", "Email", "Resumo"), show="headings")
        for col in ("ID", "Nome", "Email", "Resumo"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.grid(row=7, column=0, columnspan=2, pady=10)

        self.carregar_atendimentos()

    def adicionar_atendimento(self):
        """Salva o atendimento no banco de dados"""
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        descricao = self.entry_descricao.get("1.0", "end").strip()

        if not nome or not email or not descricao:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
            return

        try:
            conn = conectar_bd()
            if conn is None:
                return
            cur = conn.cursor()

            cur.execute("INSERT INTO atendimento (cliente, email, resumo_conversa) VALUES (%s, %s, %s)", (nome, email, descricao))
            conn.commit()
            messagebox.showinfo("Sucesso", "Atendimento registrado com sucesso!")

            # Limpar campos
            self.entry_nome.delete(0, "end")
            self.entry_email.delete(0, "end")
            self.entry_descricao.delete("1.0", "end")

            self.carregar_atendimentos()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar atendimento: {e}")
        finally:
            if conn:
                conn.close()

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
