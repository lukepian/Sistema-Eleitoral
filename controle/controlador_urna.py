from limite.tela_urna import TelaUrna
from entidade.urna import Urna


# noinspection PyArgumentList
class ControladorUrna:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__urnas = []
        self.__tela_urna = TelaUrna()

    @property
    def urnas(self):
        return self.__urnas

    def inclui_urna(self):
        dados_urna = self.__tela_urna.pega_dados_urna()
        centro = dados_urna[1]
        turno = dados_urna[2]
        codigo = dados_urna[3]
        existe = False
        for urna in self.__urnas:
            if urna.codigo == codigo:
                existe = True
                break
        if existe:
            raise Exception("Código já em uso por outra urna!")
        else:
            self.__urnas.append(Urna(centro, turno, codigo))
            self.__tela_urna.mensagem(1)
            self.opcoes()

    def exclui_urna(self):
        urna_selecionada = None
        codigo = self.__tela_urna.pega_codigo_urna()
        existe = False
        for urna in self.__urnas:
            if urna.codigo == codigo:
                existe = True
                urna_selecionada = urna
        if not existe:
            raise Exception("Urna não existente!")
        elif existe and urna_selecionada.homologacao:
            raise Exception("Votação em progresso, exclusão não é possível")
        else:
            self.__urnas.remove(urna_selecionada)
            self.__tela_urna.mensagem(2)
            self.opcoes()

    def altera_urna(self):
        urna_alterada = None
        codigo = self.__tela_urna.pega_codigo_urna()
        existe = False
        for urna in self.__urnas:
            if urna.codigo == codigo:
                urna_alterada = urna
                existe = True
        if not existe:
            raise Exception("Urna não existente!")
        else:
            self.__tela_urna.mensagem(4)
            dados_urna = self.__tela_urna.pega_dados_urna()
            centro = dados_urna[1]
            turno = dados_urna[2]
            codigo = dados_urna[3]
            existe = False
            for urna in self.__urnas:
                if urna.codigo == codigo and urna_alterada != urna:
                    existe = True
                    break
            if existe:
                raise Exception("Código já em uso por outra urna!")
            else:
                urna_alterada.centro = centro
                urna_alterada.turno = turno
                urna_alterada.codigo = codigo
                self.__tela_urna.mensagem(3)
                self.opcoes()

    def lista_urnas(self):
        dados_urnas = []
        for urna in self.__urnas:
            dados_urnas.append(urna.centro)
            dados_urnas.append(urna.turno)
            dados_urnas.append(str(urna.codigo))
        self.__tela_urna.mostra_urnas(dados_urnas)
        self.opcoes()

    def acessa_urna(self):
        urna_selecionada = None
        codigo = self.__tela_urna.pega_codigo_urna()
        existe = False
        for urna in self.__urnas:
            if urna.codigo == codigo:
                existe = True
                urna_selecionada = urna
                break
        if not existe:
            raise Exception("Urna não existente!")
        else:
            self.opcoes_urna(urna_selecionada)

    def cadastra_eleitor_urna(self, urna):
        eleitor_selecionado = None
        id_eleitor = self.__tela_urna.pega_cpf()
        existe = False
        for eleitor in self.__cont_principal.cont_eleitor.eleitores:
            if eleitor.cpf == id_eleitor:
                existe = True
                eleitor_selecionado = eleitor
                break
        if not existe:
            for candidato in self.__cont_principal.cont_candidato.candidatos:
                if candidato.cpf == id_eleitor:
                    existe = True
                    eleitor_selecionado = candidato
                    break
            if not existe:
                raise Exception("Eleitor não existente!")
            else:
                urna.cadastrar_eleitor(eleitor_selecionado)
                self.__tela_urna.mensagem(1)
                self.opcoes_urna(urna)
        else:
            urna.cadastrar_eleitor(eleitor_selecionado)
            self.__tela_urna.mensagem(1)
            self.opcoes_urna(urna)

    def exclui_eleitor_urna(self, urna):
        eleitor_selecionado = None
        id_eleitor = self.__tela_urna.pega_cpf()
        existe = False
        for eleitor in self.__cont_principal.cont_eleitor.eleitores:
            if eleitor.cpf == id_eleitor:
                existe = True
                eleitor_selecionado = eleitor
                break
        if not existe:
            for candidato in self.__cont_principal.cont_candidato.candidatos:
                if candidato.cpf == id_eleitor:
                    existe = True
                    eleitor_selecionado = candidato
                    break
            if not existe:
                raise Exception("Eleitor não existente!")
            else:
                urna.excluir_eleitor(eleitor_selecionado)
                self.__tela_urna.mensagem(2)
                self.opcoes_urna(urna)
        else:
            urna.excluir_eleitor(eleitor_selecionado)
            self.__tela_urna.mensagem(2)
            self.opcoes_urna(urna)

    def cadastra_candidato_urna(self, urna):
        candidato_selecionado = None
        id_candidato = self.__tela_urna.pega_cpf()
        existe = False
        for candidato in self.__cont_principal.cont_candidato.candidatos:
            if candidato.cpf == id_candidato:
                existe = True
                candidato_selecionado = candidato
                break
        if not existe:
            raise Exception("Candidato não existente!")
        else:
            urna.cadastrar_candidato(candidato_selecionado)
            self.__tela_urna.mensagem(1)
            self.opcoes_urna(urna)

    def exclui_candidato_urna(self, urna):
        candidato_selecionado = None
        id_candidato = self.__tela_urna.pega_cpf()
        existe = False
        for candidato in self.__cont_principal.cont_candidato.candidatos:
            if candidato.cpf == id_candidato:
                existe = True
                candidato_selecionado = candidato
                break
        if not existe:
            raise Exception("Candidato não existente!")
        else:
            urna.excluir_candidato(candidato_selecionado)
            self.__tela_urna.mensagem(2)
            self.opcoes_urna(urna)

    def homologa_urna(self, urna):
        if urna.homologacao:
            raise Exception("Urna já homologada!")
        else:
            if len(urna.eleitores_autorizados) > 0 and len(urna.candidatos_disponiveis) > 0:
                urna.homologacao = True
                self.__tela_urna.mensagem(5)
                self.opcoes_urna(urna)
            else:
                raise Exception("Número de eleitores e candidatos cadastrados insuficiente para homologação!")

    def voto_urna(self, urna):
        eleitor_votante = None
        id_eleitor = self.__tela_urna.pega_cpf()
        existe = False
        for eleitor in urna.eleitores_autorizados:
            if eleitor.cpf == id_eleitor:
                existe = True
                eleitor_votante = eleitor
                break
        if existe and eleitor_votante not in urna.eleitores_votantes:
            for cargo in self.__cont_principal.cont_cargo.cargos:
                voto_ok = False
                while not voto_ok:
                    candidato_escolhido = None
                    numero_voto = self.__tela_urna.pega_numero_voto(cargo.nome)
                    if numero_voto == "00":
                        candidato_escolhido = "Voto em Branco"
                        voto_ok = self.__tela_urna.confirma_voto(candidato_escolhido)
                        if voto_ok:
                            urna.incluir_voto(cargo, candidato_escolhido, eleitor_votante.tipo_eleitor)
                    elif numero_voto == "99":
                        candidato_escolhido = "Voto Nulo"
                        voto_ok = self.__tela_urna.confirma_voto(candidato_escolhido)
                        if voto_ok:
                            urna.incluir_voto(cargo, candidato_escolhido, eleitor_votante.tipo_eleitor)
                    else:
                        existe = False
                        for candidato in urna.candidatos_disponiveis:
                            if candidato.numero == numero_voto and candidato.cargo == cargo:
                                existe = True
                                candidato_escolhido = candidato
                                break
                        if existe:
                            voto_ok = self.__tela_urna.confirma_voto(candidato_escolhido.nome)
                            if voto_ok:
                                urna.incluir_voto(cargo, candidato_escolhido, eleitor_votante.tipo_eleitor)
                        else:
                            self.__tela_urna.mensagem(6)
            self.__tela_urna.mensagem(7)
            urna.add_eleitor_votante(eleitor_votante)
            self.opcoes_urna(urna)
        elif existe and eleitor_votante in urna.eleitores_votantes:
            raise Exception("Eleitor já votou!")
        else:
            raise Exception("Eleitor não existente ou não autorizado nesta urna!")

    def apura_votos_urna(self, urna):
        totais = {}
        for tipo_eleitor in self.__cont_principal.cont_tipo_eleitor.tipos_eleitor:
            nome = tipo_eleitor.nome
            total = tipo_eleitor.total_eleitores
            totais[nome] = total
        for cargo in self.__cont_principal.cont_cargo.cargos:
            lista_votos = urna.resultado_por_cargo(cargo)
            resultado = {}
            for voto in lista_votos:
                tipo_nome = voto.tipo_eleitor.nome
                tipo_total = totais[tipo_nome]
                pontuacao = 1/tipo_total
                if isinstance(voto.candidato, str):
                    candidato = voto.candidato
                else:
                    candidato = voto.candidato.nome
                if candidato in resultado:
                    resultado[candidato] = resultado[candidato] + pontuacao
                else:
                    resultado[candidato] = pontuacao
            mais_votos = 0
            vencedor = None
            for candidato in resultado:
                votos_inteiro = round(resultado[candidato])
                resultado[candidato] = votos_inteiro
                if votos_inteiro > mais_votos:
                    mais_votos = votos_inteiro
                    vencedor = candidato
            resultado_ordenado = sorted(resultado.items(), key=lambda x: x[1], reverse=True)
            resultado_ordenado = dict(resultado_ordenado)
            self.__tela_urna.mostra_resultado_urna(resultado_ordenado, vencedor, cargo.nome)
        urna.homologacao = False
        self.__tela_urna.mensagem(8)
        self.opcoes_urna(urna)

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_urna, 2: self.exclui_urna, 3: self.altera_urna,
                      4: self.lista_urnas, 5: self.acessa_urna, 0: self.retorna}
            opcao = self.__tela_urna.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_urna.mostra_erro(e)

    def opcoes_urna(self, urna):
        while True:
            opcoes_urna = {1: self.cadastra_eleitor_urna, 2: self.exclui_eleitor_urna,
                           3: self.cadastra_candidato_urna, 4: self.exclui_candidato_urna,
                           5: self.homologa_urna, 6: self.voto_urna,
                           7: self.apura_votos_urna}
            opcao = self.__tela_urna.mostra_opcoes_urna()
            try:
                if opcao == 0:
                    self.opcoes()
                elif 0 < opcao < 5 and urna.homologacao:
                    raise Exception("Ação indisponível enquanto votação estiver ocorrendo")
                elif opcao > 5 and not urna.homologacao:
                    raise Exception("Ação indisponível enquanto urna não estiver homologada")
                else:
                    opcoes_urna[opcao](urna)
            except Exception as e:
                self.__tela_urna.mostra_erro(e)
