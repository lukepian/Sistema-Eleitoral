from limite.tela_eleitor import TelaEleitor
from entidade.eleitor import Eleitor


class ControladorEleitor:
    def __init__(self, cont_principal):
        self.__cont_principal = cont_principal
        self.__tela_eleitor = TelaEleitor()
        self.__eleitores = []

    @property
    def eleitores(self):
        return self.__eleitores

    def inclui_eleitor(self):
        dados_eleitor = self.__tela_eleitor.pega_dados_eleitor()
        nome = dados_eleitor[1]
        cpf = dados_eleitor[2]
        tipo_eleitor = dados_eleitor[3]
        existe = False
        for eleitor in self.__eleitores:
            if eleitor.nome == nome or eleitor.cpf == cpf:
                existe = True
                break
        for candidato in self.__cont_principal.cont_candidato.candidatos:
            if candidato.nome == nome or candidato.cpf == cpf:
                existe = True
                break
        if existe:
            raise Exception("Nome ou CPF já em uso por outro cadastro!")
        else:
            existe = False
            for tipo in self.__cont_principal.cont_tipo_eleitor.tipos_eleitor:
                if tipo.nome == tipo_eleitor:
                    existe = True
                    tipo_eleitor = tipo
                    break
            if existe:
                novo_eleitor = Eleitor(nome, cpf, tipo_eleitor)
                self.__eleitores.append(novo_eleitor)
                tipo_eleitor.incluir_eleitor(novo_eleitor)
                self.__tela_eleitor.mensagem(1)
                self.opcoes()
            else:
                raise Exception("Tipo de Eleitor não existente!")

    def exclui_eleitor(self):
        id_eleitor = self.__tela_eleitor.pega_cpf()
        existe = False
        for eleitor in self.__eleitores:
            if eleitor.cpf == id_eleitor:
                existe = True
                self.__eleitores.remove(eleitor)
                eleitor.tipo_eleitor.excluir_eleitor(eleitor)
        if existe:
            self.__tela_eleitor.mensagem(2)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def altera_eleitor(self):
        eleitor_alterado = None
        id_eleitor = self.__tela_eleitor.pega_cpf()
        existe = False
        for eleitor in self.__eleitores:
            if eleitor.cpf == id_eleitor:
                eleitor_alterado = eleitor
                existe = True
        if not existe:
            raise Exception("Cadastro não existente!")
        else:
            self.__tela_eleitor.mensagem(4)
            dados_eleitor = self.__tela_eleitor.pega_dados_eleitor()
            nome = dados_eleitor[1]
            cpf = dados_eleitor[2]
            tipo_eleitor = dados_eleitor[3]
            existe = False
            for eleitor in self.__eleitores:
                if (eleitor.nome == nome or eleitor.cpf == cpf) and eleitor_alterado != eleitor:
                    existe = True
                    break
            for candidato in self.__cont_principal.cont_candidato.candidatos:
                if candidato.nome == nome or candidato.cpf == cpf:
                    existe = True
                    break
            if existe:
                raise Exception("Nome ou CPF já em uso por outro cadastro!")
            elif eleitor_alterado.tipo_eleitor.nome == tipo_eleitor:
                eleitor_alterado.nome = nome
                eleitor_alterado.cpf = cpf
                self.__tela_eleitor.mensagem(3)
                self.opcoes()
            else:
                existe = False
                for tipo in self.__cont_principal.cont_tipo_eleitor.tipos_eleitor:
                    if tipo.nome == tipo_eleitor:
                        existe = True
                        tipo_eleitor = tipo
                        break
                if existe:
                    eleitor_alterado.nome = nome
                    eleitor_alterado.cpf = cpf
                    eleitor_alterado.tipo_eleitor.excluir_eleitor(eleitor_alterado)
                    eleitor_alterado.tipo_eleitor = tipo_eleitor
                    tipo_eleitor.incluir_eleitor(eleitor_alterado)
                    self.__tela_eleitor.mensagem(3)
                    self.opcoes()
                else:
                    raise Exception("Tipo de Eleitor não existente!")

    def lista_eleitores(self):
        dados_eleitores = []
        for eleitor in self.__eleitores:
            dados_eleitores.append(eleitor.nome)
            dados_eleitores.append(eleitor.cpf)
            dados_eleitores.append(eleitor.tipo_eleitor.nome)
        self.__tela_eleitor.mostra_eleitores(dados_eleitores)
        self.opcoes()

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_eleitor, 2: self.exclui_eleitor, 3: self.altera_eleitor,
                      4: self.lista_eleitores, 0: self.retorna}
            opcao = self.__tela_eleitor.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_eleitor.mostra_erro(e)
