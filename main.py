import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from atendimento import AtendimentoFrame
from configuracoes import ConfiguracoesFrame


class ConfiguracaoFonte:
    """Gerencia o tipo e o tamanho da fonte usada na aplicação."""
    def __init__(self):
        self.fonte_familia = "Arial"
        self.fonte_tamanho = 12

    def atualizar_fonte(self, familia, tamanho):
        """Atualiza a fonte da aplicação."""
        self.fonte_familia = "Arial"
        self.fonte_tamanho = 15

    def obter_fonte(self):
        """Retorna a fonte formatada."""
        return (self.fonte_familia, self.fonte_tamanho)


class Aplicacao(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Pós Vendas 5.0")
        self.geometry("1398x800")
        self.position_center()

        # Criando o menu lateral fixo à esquerda e alinhado ao topo
        self.frame_menu = ttk.Frame(self)
        self.frame_menu.pack(side=LEFT, fill=Y, padx=10, pady=150, anchor="n")  # Alinhado ao topo

        # Criando botões de navegação (maiores e alinhados à esquerda)
        btn_config = {"padding": (30, 10), "width": 30}  # Configuração base dos botões

        self.btn_home = ttk.Button(
            self.frame_menu, text="Home", bootstyle=PRIMARY, command=self.voltar_home, **btn_config
        )
        self.btn_home.pack(fill=Y, pady=(10, 5))  # Pequeno espaçamento superior para aproximar do topo

        self.btn_atendimento = ttk.Button(
            self.frame_menu, text="Atendimento", bootstyle=PRIMARY, command=self.mostrar_atendimento, **btn_config
        )
        self.btn_atendimento.pack(pady=5)

        self.btn_configuracoes = ttk.Button(
            self.frame_menu, text="Configurações", bootstyle=PRIMARY, command=self.mostrar_configuracoes, **btn_config
        )
        self.btn_configuracoes.pack(pady=5)

        self.btn_sair = ttk.Button(
            self.frame_menu, text="Sair", bootstyle=DANGER, command=self.quit, **btn_config
        )
        self.btn_sair.pack(pady=5)

        # Criando o frame principal (vazio inicialmente)
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Inicializando os frames (mas não exibindo nenhum por padrão)
        self.frame_atendimento = AtendimentoFrame(self.frame_principal)
        self.frame_configuracoes = ConfiguracoesFrame(self.frame_principal)

    def mostrar_atendimento(self):
        """Exibe a tela de Atendimento"""
        self.ocultar_frames()
        self.frame_atendimento.pack(side=LEFT,fill=Y, padx=10, pady=50, expand=False ) #side=LEFT, fill=Y, padx=10, pady=150, anchor="n"

    def mostrar_configuracoes(self):
        """Exibe a tela de Configurações"""
        self.ocultar_frames()
        self.frame_configuracoes.pack(side=LEFT,fill=Y, padx=10, pady=50, expand=False)

    def voltar_home(self):
        """Esconde os frames ativos e retorna para a tela inicial"""
        self.ocultar_frames()

    def ocultar_frames(self):
        """Esconde todos os frames antes de exibir um novo"""
        self.frame_atendimento.pack_forget()
        self.frame_configuracoes.pack_forget()
    
    def atualizar_fonte(self, familia, tamanho):
        """Atualiza a fonte da aplicação e reflete nas telas"""
        self.config_fonte.atualizar_fonte(familia, tamanho)
        self.frame_atendimento.aplicar_fonte()
        self.frame_configuracoes.aplicar_fonte()



if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
