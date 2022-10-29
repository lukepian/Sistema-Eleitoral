from limite.tela_candidato import TelaCandidato
from entidade.candidato import Candidato


class ControladorCandidato:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__candidatos = []
        self.__tela_candidato = TelaCandidato()

    @property
    def candidatos(self):
        return self.__candidatos

    def inclui_candidato(self):
        dados_candidato = self.__tela_candidato.pega_dados_candidato()
        nome = dados_candidato[1]
        cpf = dados_candidato[2]
        tipo_eleitor = dados_candidato[3]
        numero = dados_candidato[4]
        chapa_candidato = dados_candidato[5]
        cargo_candidato = dados_candidato[6]
        existe = False
        for candidato in self.__candidatos:
            if candidato.nome == nome or candidato.cpf == cpf or candidato.numero == numero:
                existe = True
                break
        for eleitor in self.__cont_principal.cont_eleitor.eleitores:
            if eleitor.nome == nome or eleitor.cpf == cpf:
                existe = True
                break
        if existe:
            raise Exception("Nome, CPF ou número já em uso por outro cadastro!")
        else:
            existe = False
            for tipo in self.__cont_principal.cont_tipo_eleitor.tipos_eleitor:
                if tipo.nome == tipo_eleitor:
                    existe = True
                    tipo_eleitor = tipo
                    break
            if not existe:
                raise Exception("Tipo de Eleitor não existente!")
            else:
                existe = False
                for chapa in self.__cont_principal.cont_chapa.chapas:
                    if chapa.nome == chapa_candidato:
                        existe = True
                        chapa_candidato = chapa
                        break
                if not existe:
                    raise Exception("Chapa não existente!")
                else:
                    existe = False
                    for cargo in self.__cont_principal.cont_cargo.cargos:
                        if cargo.nome == cargo_candidato:
                            existe = True
                            cargo_candidato = cargo
                            break
                    if not existe:
                        raise Exception("Cargo não existente!")
                    else:
                        novo_candidato = Candidato(nome, cpf, tipo_eleitor, numero,
                                                   chapa_candidato, cargo_candidato)
                        self.__candidatos.append(novo_candidato)
                        tipo_eleitor.incluir_eleitor(novo_candidato)
                        chapa_candidato.adicionar_candidato(novo_candidato)
                        cargo_candidato.adicionar_candidato(novo_candidato)
                        self.__tela_candidato.mensagem(1)
                        self.opcoes()

    def exclui_candidato(self):
        id_candidato = self.__tela_candidato.pega_cpf()
        existe = False
        for candidato in self.__candidatos:
            if candidato.cpf == id_candidato:
                existe = True
                self.__candidatos.remove(candidato)
                candidato.tipo_eleitor.excluir_eleitor(candidato)
                candidato.chapa.remover_candidato(candidato)
                candidato.cargo.remover_candidato(candidato)
        if existe:
            self.__tela_candidato.mensagem(2)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def altera_candidato(self):
        candidato_alterado = None
        id_candidato = self.__tela_candidato.pega_cpf()
        existe = False
        for candidato in self.__candidatos:
            if candidato.cpf == id_candidato:
                candidato_alterado = candidato
                existe = True
        if not existe:
            raise Exception("Cadastro não existente!")
        else:
            self.__tela_candidato.mensagem(4)
            dados_candidato = self.__tela_candidato.pega_dados_candidato()
            nome = dados_candidato[1]
            cpf = dados_candidato[2]
            tipo_eleitor = dados_candidato[3]
            numero = dados_candidato[4]
            chapa_candidato = dados_candidato[5]
            cargo_candidato = dados_candidato[6]
            existe = False
            for candidato in self.__candidatos:
                if (candidato.nome == nome or candidato.cpf == cpf) and candidato_alterado != candidato:
                    existe = True
                    break
            for eleitor in self.__cont_principal.cont_eleitor.eleitores:
                if eleitor.nome == nome or eleitor.cpf == cpf:
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
                if not existe:
                    raise Exception("Tipo de Eleitor não existente!")
                else:
                    existe = False
                    for chapa in self.__cont_principal.cont_chapa.chapas:
                        if chapa.nome == chapa_candidato:
                            existe = True
                            chapa_candidato = chapa
                            break
                    if not existe:
                        raise Exception("Chapa não existente!")
                    else:
                        existe = False
                        for cargo in self.__cont_principal.cont_cargo.cargos:
                            if cargo.nome == cargo_candidato:
                                existe = True
                                cargo_candidato = cargo
                                break
                        if not existe:
                            raise Exception("Cargo não existente!")
                        else:
                            candidato_alterado.nome = nome
                            candidato_alterado.cpf = cpf
                            candidato_alterado.numero = numero
                            if candidato_alterado.tipo_eleitor != tipo_eleitor:
                                candidato_alterado.tipo_eleitor.excluir_eleitor(candidato_alterado)
                                candidato_alterado.tipo_eleitor = tipo_eleitor
                                tipo_eleitor.incluir_eleitor(candidato_alterado)
                            if candidato_alterado.chapa != chapa_candidato:
                                candidato_alterado.chapa.remover_candidato(candidato_alterado)
                                candidato_alterado.chapa = chapa_candidato
                                chapa_candidato.adicionar_candidato(candidato_alterado)
                            if candidato_alterado.cargo != cargo_candidato:
                                candidato_alterado.cargo.remover_candidato(candidato_alterado)
                                candidato_alterado.cargo = cargo_candidato
                                cargo_candidato.adicionar_candidato(candidato_alterado)
                            self.__tela_candidato.mensagem(3)
                            self.opcoes()

    def lista_candidatos(self):
        dados_candidatos = []
        for candidato in self.__candidatos:
            dados_candidatos.append(candidato.nome)
            dados_candidatos.append(candidato.cpf)
            dados_candidatos.append(candidato.tipo_eleitor.nome)
            dados_candidatos.append(candidato.numero)
            dados_candidatos.append(candidato.chapa.nome)
            dados_candidatos.append(candidato.cargo.nome)
        self.__tela_candidato.mostra_candidatos(dados_candidatos)
        self.opcoes()

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_candidato, 2: self.exclui_candidato, 3: self.altera_candidato,
                      4: self.lista_candidatos, 0: self.retorna}
            opcao = self.__tela_candidato.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_candidato.mostra_erro(e)
