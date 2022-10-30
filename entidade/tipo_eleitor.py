

class TipoEleitor:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__total_eleitores = 0
        self.__eleitores = []

    @property
    def nome(self):
        return self.__nome

    @property
    def total_eleitores(self):
        return self.__total_eleitores

    @property
    def eleitores(self):
        return self.__eleitores

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def incluir_eleitor(self, eleitor):
        if eleitor not in self.__eleitores:
            self.__eleitores.append(eleitor)
            self.__total_eleitores += 1

    def excluir_eleitor(self, eleitor):
        if eleitor in self.__eleitores:
            self.__eleitores.remove(eleitor)
            self.__total_eleitores -= 1
