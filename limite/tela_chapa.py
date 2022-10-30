from limite.tela import Tela


class TelaChapa(Tela):

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!"}
        print(opcoes[tipo_mensagem])

    def pega_nome_chapa(self):
        while True:
            nome_chapa = input("Digite o nome da Chapa:")
            if len(nome_chapa) > 0:
                return nome_chapa
            else:
                print("Nome inválido, tente novamente")

    def altera_nome_chapa(self):
        while True:
            nome_chapa = input("Digite o novo nome da Chapa:")
            if len(nome_chapa) > 0:
                return nome_chapa
            else:
                print("Nome inválido, tente novamente")

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
