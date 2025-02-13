import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from database import conectar_bd

class ConfiguracoesFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="Nome:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_nome = ttk.Entry(self, width=40)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Email:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_email = ttk.Entry(self, width=40)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Nova Senha:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_senha = ttk.Entry(self, width=40, show="*")
        self.entry_senha.grid(row=2, column=1, padx=5, pady=5)

        btn_salvar = ttk.Button(self, text="Salvar", bootstyle=SUCCESS, command=self.salvar_configuracoes)
        btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

    def salvar_configuracoes(self):
        """Salva ou atualiza as configurações do usuário"""
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        senha = self.entry_senha.get().strip()

        if not nome or not email:
            messagebox.showwarning("Atenção", "Nome e email são obrigatórios!")
            return

        try:
            conn = conectar_bd()
            if conn is None:
                return
            cur = conn.cursor()
            
            # Insere ou atualiza o usuário
            cur.execute(
                """
                INSERT INTO users (nome, email, senha) 
                VALUES (%s, %s, %s) 
                ON CONFLICT (email) 
                DO UPDATE SET nome = EXCLUDED.nome, senha = EXCLUDED.senha
                """,
                (nome, email, senha if senha else "default123"),
            )
            
            conn.commit()
            messagebox.showinfo("Sucesso", "Configurações atualizadas com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar configurações: {e}")
        finally:
            if conn:
                conn.close()
