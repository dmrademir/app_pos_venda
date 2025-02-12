import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from atendimento import AtendimentoFrame
from configuracoes import ConfiguracoesFrame

class Aplicacao(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Pós Vendas 5.0")
        self.geometry("1440x800")

        # Criando o frame principal (vazio inicialmente)
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Criando o menu lateral
        self.frame_menu = ttk.Frame(self)
        self.frame_menu.pack(side=LEFT, fill=Y, padx=10, pady=10)

        # Criando botões de navegação (maiores e alinhados à esquerda)
        btn_style = {"bootstyle": PRIMARY, "padding": (20, 10), "width": 20}

        self.btn_home = ttk.Button(
            self.frame_menu, text="Home", bootstyle=SUCCESS, padding=(20, 10), width=20, command=self.voltar_home
        )
        self.btn_home.pack(pady=5)

        self.btn_atendimento = ttk.Button(
            self.frame_menu, text="Atendimento", command=self.mostrar_atendimento, **btn_style
        )
        self.btn_atendimento.pack(pady=5)

        self.btn_configuracoes = ttk.Button(
            self.frame_menu, text="Configurações", command=self.mostrar_configuracoes, **btn_style
        )
        self.btn_configuracoes.pack(pady=5)

        self.btn_sair = ttk.Button(
            self.frame_menu, text="Sair", bootstyle=DANGER, padding=(20, 10), width=20, command=self.quit
        )
        self.btn_sair.pack(pady=5)

        # Inicializando os frames (mas não exibindo nenhum por padrão)
        self.frame_atendimento = AtendimentoFrame(self.frame_principal)
        self.frame_configuracoes = ConfiguracoesFrame(self.frame_principal)

    def mostrar_atendimento(self):
        """Exibe a tela de Atendimento"""
        self.ocultar_frames()
        self.frame_atendimento.pack(fill=BOTH, expand=True)

    def mostrar_configuracoes(self):
        """Exibe a tela de Configurações"""
        self.ocultar_frames()
        self.frame_configuracoes.pack(fill=BOTH, expand=True)

    def voltar_home(self):
        """Esconde os frames ativos e retorna para a tela inicial"""
        self.ocultar_frames()

    def ocultar_frames(self):
        """Esconde todos os frames antes de exibir um novo"""
        self.frame_atendimento.pack_forget()
        self.frame_configuracoes.pack_forget()

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
