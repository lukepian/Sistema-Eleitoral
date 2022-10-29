import sys
from limite.tela_principal import TelaPrincipal
from controle.controlador_eleitor import ControladorEleitor
from controle.controlador_candidato import ControladorCandidato
from controle.controlador_tipo_eleitor import ControladorTipoEleitor
from controle.controlador_chapa import ControladorChapa
from controle.controlador_cargo import ControladorCargo
from controle.controlador_urna import ControladorUrna


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaPrincipal()
        self.__cont_eleitor = ControladorEleitor(self)
        self.__cont_candidato = ControladorCandidato(self)
        self.__cont_tipo_eleitor = ControladorTipoEleitor(self)
        self.__cont_chapa = ControladorChapa(self)
        self.__cont_cargo = ControladorCargo(self)
        self.__cont_urna = ControladorUrna(self)

    @property
    def cont_eleitor(self):
        return self.__cont_eleitor

    @property
    def cont_candidato(self):
        return self.__cont_candidato

    @property
    def cont_tipo_eleitor(self):
        return self.__cont_tipo_eleitor

    @property
    def cont_chapa(self):
        return self.__cont_chapa

    @property
    def cont_cargo(self):
        return self.__cont_cargo

    @property
    def cont_urna(self):
        return self.__cont_urna

    def encerra(self):
        sys.exit()

    def inicializa(self):
        opcoes = {1: self.cont_eleitor.opcoes, 2: self.cont_candidato.opcoes,
                  3: self.cont_tipo_eleitor.opcoes, 4: self.cont_chapa.opcoes,
                  5: self.cont_cargo.opcoes, 6: self.cont_urna.opcoes, 0: self.encerra}
        opcao = self.__tela_principal.mostra_opcoes()
        opcoes[opcao]()
