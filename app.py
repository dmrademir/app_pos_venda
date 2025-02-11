import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
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

# Função para adicionar atendimento
def adicionar_atendimento():
    nome = entry_nome.get()
    email = entry_email.get()
    descricao = entry_descricao.get("1.0", ttk.END).strip()

    if not nome or not email or not descricao:
        messagebox.showwarning("Campos obrigatórios", "Preencha todos os campos!")
        return

    try:
        conn = conectar_bd()
        if conn is None:
            return
        cur = conn.cursor()

        # Verifica se o cliente já existe
        cur.execute("SELECT id FROM clientes WHERE email = %s", (email,))
        cliente = cur.fetchone()
        if not cliente:
            cur.execute(
                "INSERT INTO clientes (nome, email) VALUES (%s, %s) RETURNING id",
                (nome, email),
            )
            cliente_id = cur.fetchone()[0]
        else:
            cliente_id = cliente[0]

        # Adiciona o atendimento
        cur.execute(
            "INSERT INTO atendimentos (cliente_id, descricao, status) VALUES (%s, %s, %s)",
            (cliente_id, descricao, "Aberto"),
        )
        conn.commit()
        messagebox.showinfo("Sucesso", "Atendimento adicionado com sucesso!")
        entry_nome.delete(0, ttk.END)
        entry_email.delete(0, ttk.END)
        entry_descricao.delete("1.0", ttk.END)
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
        cur.execute("""
            SELECT a.id, c.nome, a.descricao, a.status 
            FROM atendimentos a 
            JOIN clientes c ON a.cliente_id = c.id
        """)
        for row in cur.fetchall():
            tree.insert("", ttk.END, values=row)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar atendimentos: {e}")
    finally:
        if conn:
            conn.close()

# Criação da interface gráfica
root = ttk.Window(themename="solar")
root.title("Pós Vendas 5.0")

# Formulário de Atendimento
frame_form = ttk.Frame(root, padding=10)
frame_form.pack(pady=10)

ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
entry_nome = ttk.Entry(frame_form)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
entry_email = ttk.Entry(frame_form)
entry_email.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text="Descrição:").grid(row=2, column=0, padx=5, pady=5, sticky=W)
entry_descricao = ttk.Text(frame_form, height=5, width=40)
entry_descricao.grid(row=2, column=1, padx=5, pady=5)

btn_adicionar = ttk.Button(frame_form, text="Adicionar Atendimento", command=adicionar_atendimento, bootstyle=SUCCESS)
btn_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

# Tabela de Atendimentos
frame_table = ttk.Frame(root, padding=10)
frame_table.pack()

columns = ("ID", "Cliente", "Descrição", "Status")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", bootstyle=INFO)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack()

carregar_atendimentos()

# Executa a aplicação
root.mainloop()
