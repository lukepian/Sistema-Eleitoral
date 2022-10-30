from entidade.eleitor import Eleitor


class Candidato(Eleitor):
    def __init__(self, nome: str, cpf: str, tipo_eleitor,
                 numero, chapa, cargo):
        super().__init__(nome, cpf, tipo_eleitor)
        self.__numero = numero
        self.__chapa = chapa
        self.__cargo = cargo

    @property
    def numero(self):
        return self.__numero

    @property
    def chapa(self):
        return self.__chapa

    @property
    def cargo(self):
        return self.__cargo

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @chapa.setter
    def chapa(self, chapa):
        self.__chapa = chapa

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
