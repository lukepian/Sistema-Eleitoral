from entidade.eleitor import Eleitor


class Candidato(Eleitor):
    def __init__(self, nome: str, cpf: str, tipo_eleitor,
                 numero, chapa, cargo):
        super().__init__(nome, cpf, tipo_eleitor)
        self.__nome = nome
        self.__cpf = cpf
        self.__tipo_eleitor = tipo_eleitor
        self.__numero = numero
        self.__chapa = chapa
        self.__cargo = cargo

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @property
    def numero(self):
        return self.__numero

    @property
    def chapa(self):
        return self.__chapa

    @property
    def cargo(self):
        return self.__cargo

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @chapa.setter
    def chapa(self, chapa):
        self.__chapa = chapa

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
