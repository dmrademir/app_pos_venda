import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, Toplevel
import psycopg2

# Conexão com o banco de dados
def conectar_bd():
    try:
        return psycopg2.connect(
            database="pos_vendas",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para adicionar atendimento com validação
def adicionar_atendimento():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    descricao = entry_descricao.get("1.0", "end").strip()

    if not nome or not email or not descricao:
        messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
        return

    try:
        conn = conectar_bd()
        if conn is None:
            return
        cur = conn.cursor()

        # Verifica se o usuário já existe
        cur.execute("SELECT id FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        if not user:
            cur.execute(
                "INSERT INTO users (nome, email, senha) VALUES (%s, %s, %s) RETURNING id",
                (nome, email, "default123"),
            )
            user_id = cur.fetchone()[0]
        else:
            user_id = user[0]

        # Adiciona o atendimento
        cur.execute(
            "INSERT INTO atendimento (user_id, cliente, email, resumo_conversa) VALUES (%s, %s, %s, %s)",
            (user_id, nome, email, descricao),
        )
        conn.commit()
        messagebox.showinfo("Sucesso", "Atendimento registrado com sucesso!")
        entry_nome.delete(0, "end")
        entry_email.delete(0, "end")
        entry_descricao.delete("1.0", "end")
        carregar_atendimentos()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao adicionar atendimento: {e}")
    finally:
        if conn:
            conn.close()

# Função para carregar atendimentos na tabela
def carregar_atendimentos():
    for row in tree.get_children():
        tree.delete(row)

    try:
        conn = conectar_bd()
        if conn is None:
            return
        cur = conn.cursor()
        cur.execute("SELECT id, cliente, email, resumo_conversa FROM atendimento")
        for row in cur.fetchall():
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar atendimentos: {e}")
    finally:
        if conn:
            conn.close()

# Tela de Configurações do Usuário
def abrir_configuracoes():
    config_window = Toplevel(root)
    config_window.title("Configurações do Usuário")
    config_window.geometry("350x250")

    ttk.Label(config_window, text="Nome:", font=("Arial", 10)).pack(pady=5)
    entry_nome_config = ttk.Entry(config_window, width=40)
    entry_nome_config.pack()

    ttk.Label(config_window, text="Email:", font=("Arial", 10)).pack(pady=5)
    entry_email_config = ttk.Entry(config_window, width=40)
    entry_email_config.pack()

    ttk.Label(config_window, text="Nova Senha:", font=("Arial", 10)).pack(pady=5)
    entry_senha_config = ttk.Entry(config_window, width=40, show="*")
    entry_senha_config.pack()

    def salvar_configuracoes():
        nome = entry_nome_config.get().strip()
        email = entry_email_config.get().strip()
        senha = entry_senha_config.get().strip()

        if not nome or not email:
            messagebox.showwarning("Atenção", "Nome e email são obrigatórios!")
            return

        try:
            conn = conectar_bd()
            if conn is None:
                return
            cur = conn.cursor()
            
            # Atualiza ou insere o usuário no banco
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
            config_window.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar configurações: {e}")
        finally:
            if conn:
                conn.close()

    btn_salvar = ttk.Button(config_window, text="Salvar", bootstyle=SUCCESS, command=salvar_configuracoes)
    btn_salvar.pack(pady=10)

# Interface principal
root = ttk.Window(themename="superhero")
root.title("Pós Vendas 5.0")
root.geometry("1440x650")

# Menu
menu_bar = ttk.Menu(root)
root.config(menu=menu_bar)
menu_opcoes = ttk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Opções", menu=menu_opcoes)
menu_opcoes.add_command(label="Configurações do Usuário", command=abrir_configuracoes)
menu_opcoes.add_separator()
menu_opcoes.add_command(label="Sair", command=root.quit)

# Formulário de Atendimento
frame_form = ttk.Frame(root)
frame_form.pack(pady=10)

# Nome
ttk.Label(frame_form, text="Nome:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_nome = ttk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

# Email
ttk.Label(frame_form, text="Email:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_email = ttk.Entry(frame_form, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# CNPJ
ttk.Label(frame_form, text="CNPJ:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_cnpj = ttk.Entry(frame_form, width=40)
entry_cnpj.grid(row=2, column=1, padx=5, pady=5)

# Cidade
ttk.Label(frame_form, text="Cidade:", font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_cidade = ttk.Entry(frame_form, width=40)
entry_cidade.grid(row=3, column=1, padx=5, pady=5)

# UF
ttk.Label(frame_form, text="UF:", font=("Arial", 10)).grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_uf = ttk.Entry(frame_form, width=5)
entry_uf.grid(row=4, column=1, padx=5, pady=5, sticky="w")

# Telefone de Contato
ttk.Label(frame_form, text="Telefone de Contato:", font=("Arial", 10)).grid(row=5, column=0, padx=5, pady=5, sticky="w")
entry_telefone = ttk.Entry(frame_form, width=40)
entry_telefone.grid(row=5, column=1, padx=5, pady=5)

# Nota Fiscal
ttk.Label(frame_form, text="Nota Fiscal:", font=("Arial", 10)).grid(row=6, column=0, padx=5, pady=5, sticky="w")
entry_nota_fiscal = ttk.Entry(frame_form, width=40)
entry_nota_fiscal.grid(row=6, column=1, padx=5, pady=5)

# Valor
ttk.Label(frame_form, text="Valor:", font=("Arial", 10)).grid(row=7, column=0, padx=5, pady=5, sticky="w")
entry_valor = ttk.Entry(frame_form, width=40)
entry_valor.grid(row=7, column=1, padx=5, pady=5)

# Resumo da Conversa
ttk.Label(frame_form, text="Resumo da Conversa:", font=("Arial", 10)).grid(row=8, column=0, padx=5, pady=5, sticky="w")
entry_resumo = ttk.Text(frame_form, height=5, width=40)
entry_resumo.grid(row=8, column=1, padx=5, pady=5)

btn_adicionar = ttk.Button(frame_form, text="Adicionar Atendimento", bootstyle=SUCCESS, command=adicionar_atendimento)
btn_adicionar.grid(row=10, column=0, columnspan=2, pady=10)

# Tabela de Atendimentos
frame_table = ttk.Frame(root)
frame_table.pack(pady=10)

columns = ("ID", "Cliente", "Email", "Resumo")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", bootstyle=INFO)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack()

# Carrega os atendimentos
carregar_atendimentos()


# Executa a aplicação
root.mainloop()
