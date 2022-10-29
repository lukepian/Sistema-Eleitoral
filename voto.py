

class Voto:
    def __init__(self, cargo, candidato, tipo_eleitor):
        self.__cargo = cargo
        self.__candidato = candidato
        self.__tipo_eleitor = tipo_eleitor

    @property
    def cargo(self):
        return self.__cargo

    @property
    def candidato(self):
        return self.__candidato

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor
