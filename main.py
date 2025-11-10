import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from atendimento_frame import AtendimentoFrame

class Aplicacao(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("Pós Vendas 6.0")
        self.geometry("1600x900")
        self.position_center()

        # Frame de menu lateral
        self.frame_menu = ttk.Frame(self)
        self.frame_menu.pack(side=LEFT, fill=Y, padx=10, pady=150, anchor="n")

        btn_config = {"padding": (30, 10), "width": 30}

        self.btn_home = ttk.Button(
            self.frame_menu, text="Home", bootstyle=PRIMARY,
            command=self.voltar_home, **btn_config
        )
        self.btn_home.pack(pady=(10, 5))

        self.btn_atendimento = ttk.Button(
            self.frame_menu, text="Atendimento", bootstyle=PRIMARY,
            command=self.mostrar_atendimento, **btn_config
        )
        self.btn_atendimento.pack(pady=5)

        self.btn_sair = ttk.Button(
            self.frame_menu, text="Sair", bootstyle=DANGER,
            command=self.quit, **btn_config
        )
        self.btn_sair.pack(pady=5)

        # Frame principal onde os conteúdos aparecerão
        self.frame_principal = ttk.Frame(self)
        self.frame_principal.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Instância do frame de atendimento
        self.frame_atendimento = AtendimentoFrame(self.frame_principal)

    def mostrar_atendimento(self):
        self.ocultar_frames()
        self.frame_atendimento.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def voltar_home(self):
        self.ocultar_frames()

    def ocultar_frames(self):
        self.frame_atendimento.pack_forget()


if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()
