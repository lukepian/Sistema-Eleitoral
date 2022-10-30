from entidade.voto import Voto


class Urna:
    def __init__(self, centro: str, turno: str, codigo: int):
        self.__centro = centro
        self.__turno = turno
        self.__codigo = codigo
        self.__homologacao = False
        self.__votos = []
        self.__eleitores_autorizados = []
        self.__candidatos_disponiveis = []
        self.__eleitores_votantes = []

    @property
    def centro(self):
        return self.__centro

    @property
    def turno(self):
        return self.__turno

    @property
    def codigo(self):
        return self.__codigo

    @property
    def homologacao(self):
        return self.__homologacao

    @property
    def eleitores_autorizados(self):
        return self.__eleitores_autorizados

    @property
    def candidatos_disponiveis(self):
        return self.__candidatos_disponiveis

    @property
    def eleitores_votantes(self):
        return self.__eleitores_votantes

    @centro.setter
    def centro(self, centro):
        self.__centro = centro

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @homologacao.setter
    def homologacao(self, homologacao):
        self.__homologacao = homologacao

    def cadastrar_eleitor(self, eleitor):
        if eleitor not in self.__eleitores_autorizados:
            self.__eleitores_autorizados.append(eleitor)
        else:
            raise Exception("Eleitor já cadastrado!")

    def excluir_eleitor(self, eleitor):
        if eleitor in self.__eleitores_autorizados:
            self.__eleitores_autorizados.remove(eleitor)
        else:
            raise Exception("Eleitor não cadastrado!")

    def cadastrar_candidato(self, candidato):
        if candidato not in self.__candidatos_disponiveis:
            self.__candidatos_disponiveis.append(candidato)
        else:
            raise Exception("Candidato já cadastrado!")

    def excluir_candidato(self, candidato):
        if candidato in self.__candidatos_disponiveis:
            self.__candidatos_disponiveis.remove(candidato)
        else:
            raise Exception("Candidato não cadastrado!")

    def incluir_voto(self, cargo, candidato, tipo_eleitor):
        self.__votos.append(Voto(cargo, candidato, tipo_eleitor))

    def add_eleitor_votante(self, eleitor):
        self.__eleitores_votantes.append(eleitor)

    def resultado_por_cargo(self, cargo):
        lista_votos = []
        for voto in self.__votos:
            if voto.cargo == cargo:
                lista_votos.append(voto)
        return lista_votos
