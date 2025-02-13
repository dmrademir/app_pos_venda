import ttkbootstrap as tb
from tkinter import Frame, Label

# Criando a aplicação principal
root = tb.Window(themename="darkly")
root.title("Sistema de Atendimento")
root.geometry("600x400")

# Dicionário para armazenar os frames (telas)
frames = {}

# Função para alternar entre as telas
def show_frame(frame_name):
    for frame in frames.values():
        frame.pack_forget()
    frames[frame_name].pack(fill="both", expand=True)

# Criando um Frame para o menu lateral
menu_frame = Frame(root, bg="#222", width=150)
menu_frame.pack(side="left", fill="y")

# Criando os botões do menu
btn_atendimento = tb.Button(menu_frame, text="Atendimento", bootstyle="primary", command=lambda: show_frame("atendimento"))
btn_atendimento.pack(fill="x", pady=5, padx=10)

btn_config = tb.Button(menu_frame, text="Configurações", bootstyle="secondary", command=lambda: show_frame("config"))
btn_config.pack(fill="x", pady=5, padx=10)

btn_sair = tb.Button(menu_frame, text="Sair", bootstyle="danger", command=root.quit)
btn_sair.pack(fill="x", pady=5, padx=10)

# Criando os frames das telas
frames["atendimento"] = Frame(root, bg="white")
Label(frames["atendimento"], text="Tela de Atendimento", font=("Arial", 16)).pack(pady=50)

frames["config"] = Frame(root, bg="white")
Label(frames["config"], text="Tela de Configurações", font=("Arial", 16)).pack(pady=50)

# Exibir a tela inicial
show_frame("atendimento")

# Iniciando o loop principal
root.mainloop()
