

class Chapa:
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
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def adicionar_candidato(self, candidato):
        if candidato not in self.__candidatos:
            self.__candidatos.append(candidato)
        else:
            raise Exception("Candidato já cadastrado na chapa!")

    def remover_candidato(self, candidato):
        if candidato in self.__candidatos:
            self.__candidatos.remove(candidato)
        else:
            raise Exception("Candidato não cadastrado na chapa!")
