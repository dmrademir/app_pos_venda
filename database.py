import psycopg2
from tkinter import messagebox

def conectar_bd():
    """Conecta ao banco de dados PostgreSQL e retorna a conexão"""
    try:
        # Substitua com seus próprios parâmetros de conexão
        conn = psycopg2.connect(
            database="pos_vendas",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        return conn
    except psycopg2.DatabaseError as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {e}")
        return None
