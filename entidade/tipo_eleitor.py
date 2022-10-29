

class TipoEleitor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__eleitores = []

    @property
    def nome(self):
        return self.__nome

    @property
    def eleitores(self):
        return self.__eleitores

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def incluir_eleitor(self, eleitor):
        if eleitor not in self.__eleitores:
            self.__eleitores.append(eleitor)

    def excluir_eleitor(self, eleitor):
        if eleitor in self.__eleitores:
            self.__eleitores.remove(eleitor)

    def total_eleitores(self):
        total = len(self.__eleitores)
        return total
