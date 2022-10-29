from limite.tela_chapa import TelaChapa
from entidade.chapa import Chapa


class ControladorChapa:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__chapas = []
        self.__tela_chapa = TelaChapa()

    @property
    def chapas(self):
        return self.__chapas

    def inclui_chapa(self):
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        existe = False
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                existe = True
                break
        if existe:
            raise Exception("Cadastro já existente!")
        else:
            self.__chapas.append(Chapa(nome_chapa))
            self.__tela_chapa.mensagem(1)
            self.opcoes()

    def exclui_chapa(self):
        chapa_selecionada = None
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        existe = False
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                existe = True
                chapa_selecionada = chapa
                break
        if existe and len(chapa_selecionada.candidatos) > 0:
            raise Exception("Chapa selecionado tem candidatos associados, exclusão não é possível")
        elif existe and len(chapa_selecionada.candidatos) == 0:
            self.__chapas.remove(chapa_selecionada)
            self.__tela_chapa.mensagem(2)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def altera_chapa(self):
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        existe = False
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                existe = True
                novo_nome = self.__tela_chapa.altera_nome_chapa()
                chapa.nome = novo_nome
                self.__tela_chapa.mensagem(3)
                break
        if existe:
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def lista_chapas(self):
        chapas = []
        for chapa in self.__chapas:
            chapas.append(chapa.nome)
        self.__tela_chapa.mostra_chapas(chapas)
        self.opcoes()

    def lista_candidatos_chapa(self):
        chapa_selecionada = None
        nome_chapa = self.__tela_chapa.pega_nome_chapa()
        existe = False
        for chapa in self.__chapas:
            if chapa.nome == nome_chapa:
                existe = True
                chapa_selecionada = chapa
                break
        if existe:
            lista_candidatos = []
            for candidato in chapa_selecionada.candidatos:
                lista_candidatos.append(candidato.nome)
            self.__tela_chapa.mostra_candidatos_chapa(lista_candidatos, nome_chapa)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_chapa, 2: self.exclui_chapa, 3: self.altera_chapa,
                      4: self.lista_chapas, 5: self.lista_candidatos_chapa, 0: self.retorna}
            opcao = self.__tela_chapa.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_chapa.mostra_erro(e)
