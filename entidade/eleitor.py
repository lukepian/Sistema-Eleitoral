

class Eleitor:
    def __init__(self, nome: str, cpf: str, tipo_eleitor):
        self.__nome = nome
        self.__cpf = cpf
        self.__tipo_eleitor = tipo_eleitor

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor
