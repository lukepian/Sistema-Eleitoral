from limite.tela_cargo import TelaCargo
from entidade.cargo import Cargo


class ControladorCargo:
    def __init__(self, controlador_principal):
        self.__cont_principal = controlador_principal
        self.__cargos = []
        self.__tela_cargo = TelaCargo()

    @property
    def cargos(self):
        return self.__cargos

    def inclui_cargo(self):
        nome_cargo = self.__tela_cargo.pega_nome_cargo()
        existe = False
        for cargo in self.__cargos:
            if cargo.nome == nome_cargo:
                existe = True
                break
        if existe:
            raise Exception("Cadastro já existente!")
        else:
            self.__cargos.append(Cargo(nome_cargo))
            self.__tela_cargo.mensagem(1)
            self.opcoes()

    def exclui_cargo(self):
        cargo_selecionado = None
        nome_cargo = self.__tela_cargo.pega_nome_cargo()
        existe = False
        for cargo in self.__cargos:
            if cargo.nome == nome_cargo:
                cargo_selecionado = cargo
                existe = True
                break
        if existe and len(cargo_selecionado.candidatos) > 0:
            raise Exception("Cargo selecionado tem candidatos associados, exclusão não é possível")
        elif existe and len(cargo_selecionado.candidatos) == 0:
            self.__cargos.remove(cargo_selecionado)
            self.__tela_cargo.mensagem(2)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def altera_cargo(self):
        nome_cargo = self.__tela_cargo.pega_nome_cargo()
        existe = False
        for cargo in self.__cargos:
            if cargo.nome == nome_cargo:
                existe = True
                novo_nome = self.__tela_cargo.altera_nome_cargo()
                cargo.nome = novo_nome
                self.__tela_cargo.mensagem(3)
                break
        if existe:
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def lista_cargos(self):
        cargos = []
        for cargo in self.__cargos:
            cargos.append(cargo.nome)
        self.__tela_cargo.mostra_cargos(cargos)
        self.opcoes()

    def lista_candidatos_cargo(self):
        cargo_selecionado = None
        nome_cargo = self.__tela_cargo.pega_nome_cargo()
        existe = False
        for cargo in self.__cargos:
            if cargo.nome == nome_cargo:
                existe = True
                cargo_selecionado = cargo
                break
        if existe:
            lista_candidatos = []
            for candidato in cargo_selecionado.candidatos:
                lista_candidatos.append(candidato.nome)
            self.__tela_cargo.mostra_candidatos_cargo(lista_candidatos, nome_cargo)
            self.opcoes()
        else:
            raise Exception("Cadastro não existente!")

    def retorna(self):
        self.__cont_principal.inicializa()

    def opcoes(self):
        while True:
            opcoes = {1: self.inclui_cargo, 2: self.exclui_cargo, 3: self.altera_cargo,
                      4: self.lista_cargos, 5: self.lista_candidatos_cargo, 0: self.retorna}
            opcao = self.__tela_cargo.mostra_opcoes()
            try:
                opcoes[opcao]()
            except Exception as e:
                self.__tela_cargo.mostra_erro(e)
