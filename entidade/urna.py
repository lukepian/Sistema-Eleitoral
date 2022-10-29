

class Urna:
    def __init__(self, centro: str, turno: str, codigo: int):
        self.__centro = centro
        self.__turno = turno
        self.__codigo = codigo
        self.__homologada = False
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
    def homologada(self):
        return self.__homologada

    @centro.setter
    def centro(self, centro):
        self.__centro = centro

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    def homologar(self):
        self.__homologada = True

    def cadastrar_eleitor(self, eleitor):
        if eleitor not in self.__eleitores_autorizados:
            self.__eleitores_autorizados.append(eleitor)

    def excluir_eleitor(self, eleitor):
        if eleitor in self.__eleitores_autorizados:
            self.__eleitores_autorizados.remove(eleitor)

    def cadastrar_candidato(self, candidato):
        if candidato not in self.__candidatos_disponiveis:
            self.__candidatos_disponiveis.append(candidato)

    def excluir_candidato(self, candidato):
        if candidato in self.__candidatos_disponiveis:
            self.__candidatos_disponiveis.remove(candidato)

    def incluir_voto(self, voto):
        self.__votos.append(voto)

    def add_eleitor_votante(self, eleitor):
        self.__eleitores_votantes.append(eleitor)

    def encerrar_votacao(self):
        self.__homologada = False

    def resultado_por_cargo(self, cargo):
        lista_votos = []
        for voto in self.__votos:
            if voto.cargo == cargo:
                lista_votos.append(voto)
        return lista_votos
