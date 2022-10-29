

class Cargo:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__candidatos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def candidatos(self):
        return self.__candidatos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def adicionar_candidato(self, candidato):
        if candidato not in self.__candidatos:
            self.__candidatos.append(candidato)

    def remover_candidato(self, candidato):
        if candidato in self.__candidatos:
            self.__candidatos.remove(candidato)
