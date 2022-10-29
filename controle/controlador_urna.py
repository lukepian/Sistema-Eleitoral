from limite.tela_urna import TelaUrna


class ControladorUrna:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__urnas = []
        self.__tela_urna = TelaUrna()

    def opcoes(self):
        opcao = self.__tela_urna.mostra_opcoes()
