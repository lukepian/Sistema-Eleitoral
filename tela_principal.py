

class TelaPrincipal:

    def pega_numero(self, lim_inf, lim_sup):
        num = int(input("Digite uma das opções:"))
        if lim_inf <= num <= lim_sup:
            return num
        else:
            raise ValueError

    def mostra_opcoes(self):
        while True:
            print("#" * 22)
            print("SISTEMA ELEITORAL UFSC")
            print("#" * 22)
            print("1 - Eleitores")
            print("2 - Candidatos")
            print("3 - Tipos de Eleitor")
            print("4 - Chapas")
            print("5 - Cargos")
            print("6 - Urnas")
            print("0 - Sair")
            try:
                opcao = self.pega_numero(0, 6)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
