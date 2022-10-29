from limite.tela_tipo_eleitor import TelaTipoEleitor
from entidade.tipo_eleitor import TipoEleitor


class ControladorTipoEleitor:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__tipos_eleitor = []
        self.__tela_tipo_eleitor = TelaTipoEleitor()

    @property
    def tipos_eleitor(self):
        return self.__tipos_eleitor

    def inclui_tipo_eleitor(self):
        nome_tipo_eleitor = self.__tela_tipo_eleitor.pega_nome_tipo_eleitor()
        existe = False
        for tipo_eleitor in self.__tipos_eleitor:
            if tipo_eleitor.nome == nome_tipo_eleitor:
                existe = True
                break
        if existe:
            raise Exception("Cadastro já existente!")
        else:
            self.__tipos_eleitor.append(TipoEleitor(nome_tipo_eleitor))
            self.__tela_tipo_eleitor.mensagem(1)
            self.opcoes()

    def exclui_tipo_eleitor(self):
        tipo_eleitor_selecionado = None
        nome_tipo_eleitor = self.__tela_tipo_eleitor.pega_nome_tipo_eleitor()
        existe = False
        for tipo_eleitor in self.__tipos_eleitor:
            if tipo_eleitor.nome == nome_tipo_eleitor:
                tipo_eleitor_selecionado = tipo_eleitor
                existe = True
                break
        if existe and len(tipo_eleitor_selecionado.eleitores) > 0:
            raise Exception("Tipo de Eleitor selecionado tem eleitores associados, exclusão não é possível")
        elif existe and len(tipo_eleitor_selecionado.eleitores) == 0:
            self.__tipos_eleitor.remove(tipo_eleitor_selecionado)
            self.__tela_tipo_eleitor.mensagem(2)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def altera_tipo_eleitor(self):
        nome_tipo_eleitor = self.__tela_tipo_eleitor.pega_nome_tipo_eleitor()
        existe = False
        for tipo_eleitor in self.__tipos_eleitor:
            if tipo_eleitor.nome == nome_tipo_eleitor:
                existe = True
                novo_nome = self.__tela_tipo_eleitor.altera_nome_tipo_eleitor()
                tipo_eleitor.nome = novo_nome
                self.__tela_tipo_eleitor.mensagem(3)
                break
        if existe:
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def lista_tipos_eleitor(self):
        tipos_eleitor = []
        for tipo_eleitor in self.__tipos_eleitor:
            tipos_eleitor.append(tipo_eleitor.nome)
        self.__tela_tipo_eleitor.mostra_tipos_eleitor(tipos_eleitor)
        self.opcoes()

    def lista_eleitores_tipo_eleitor(self):
        tipo_eleitor_selecionado = None
        nome_tipo_eleitor = self.__tela_tipo_eleitor.pega_nome_tipo_eleitor()
        existe = False
        for tipo_eleitor in self.__tipos_eleitor:
            if tipo_eleitor.nome == nome_tipo_eleitor:
                existe = True
                tipo_eleitor_selecionado = tipo_eleitor
                break
        if existe:
            lista_eleitores = []
            for eleitor in tipo_eleitor_selecionado.eleitores:
                lista_eleitores.append(eleitor.nome)
            self.__tela_tipo_eleitor.mostra_eleitores_tipo_eleitor(lista_eleitores, nome_tipo_eleitor)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_tipo_eleitor, 2: self.exclui_tipo_eleitor, 3: self.altera_tipo_eleitor,
                      4: self.lista_tipos_eleitor, 5: self.lista_eleitores_tipo_eleitor, 0: self.retorna}
            opcao = self.__tela_tipo_eleitor.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_tipo_eleitor.mostra_erro(e)
