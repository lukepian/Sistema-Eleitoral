from abc import ABC, abstractmethod


class Tela(ABC):

    def mostra_erro(self, erro):
        print(erro)

    def pega_numero(self, lim_inf, lim_sup):
        num = int(input("Digite uma das opções:"))
        if lim_inf <= num <= lim_sup:
            return num
        else:
            raise ValueError

    @abstractmethod
    def mensagem(self, tipo_mensagem: int):
        pass

    @abstractmethod
    def mostra_opcoes(self):
        pass
