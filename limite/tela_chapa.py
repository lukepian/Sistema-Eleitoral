

class TelaChapa:

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!"}
        print(opcoes[tipo_mensagem])

    def mostra_erro(self, erro):
        print(erro)

    def pega_numero(self, lim_inf, lim_sup):
        num = int(input("Digite uma das opções:"))
        if lim_inf <= num <= lim_sup:
            return num
        else:
            raise ValueError

    def pega_nome_chapa(self):
        nome_chapa = input("Digite o nome da Chapa:")
        return nome_chapa

    def altera_nome_chapa(self):
        nome_chapa = input("Digite o novo nome da Chapa:")
        return nome_chapa

    def mostra_chapas(self, chapas):
        if len(chapas) > 0:
            print("Chapas cadastradas:")
            for nome_chapa in chapas:
                print(nome_chapa)
        else:
            print("Nenhuma chapa cadastrada")

    def mostra_candidatos_chapa(self, lista_candidatos, nome_chapa):
        if len(lista_candidatos) == 0:
            print("Nenhum candidato cadastrado")
        else:
            print("Candidatos da Chapa " + nome_chapa)
            for candidato in lista_candidatos:
                print(candidato)

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Chapas")
            print("#" * 20)
            print("1 - Cadastro de Chapa")
            print("2 - Exclusão de Chapa")
            print("3 - Alteração de Chapa")
            print("4 - Listagem de Chapas")
            print("5 - Listagem de Candidatos por Chapa")
            print("0 - Retornar")
            try:
                opcao = self.pega_numero(0, 5)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
