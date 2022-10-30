from limite.tela import Tela


class TelaEleitor(Tela):

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!", 4: "A seguir, digite os novos dados"}
        print(opcoes[tipo_mensagem])

    def pega_cpf(self):
        while True:
            cpf = input("Digite o CPF:")
            if len(cpf) == 11:
                return cpf
            else:
                print("CPF inválido, tente novamente")

    def pega_dados_eleitor(self):
        while True:
            nome_eleitor = input("Digite o nome:")
            cpf_eleitor = self.pega_cpf()
            tipo_do_eleitor = input("Digite o tipo do eleitor:")
            if len(nome_eleitor) > 0:
                dados = {1: nome_eleitor, 2: cpf_eleitor, 3: tipo_do_eleitor}
                return dados
            else:
                print("Nome inválido, tente novamente")

    def mostra_eleitores(self, dados_eleitores):
        if len(dados_eleitores) == 0:
            print("Nenhum eleitor cadastrado!")
        else:
            print("Eleitores cadastrados:")
            contador = 0
            for dado in dados_eleitores:
                contador += 1
                if contador % 3 == 1:
                    print("Nome: " + dado)
                elif contador % 3 == 2:
                    print("CPF: " + dado)
                else:
                    print("Tipo de Eleitor: " + dado)
                    print()

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Eleitores")
            print("#" * 20)
            print("1 - Cadastro de Eleitor")
            print("2 - Exclusão de Eleitor")
            print("3 - Alteração de Eleitor")
            print("4 - Listagem dos Eleitores")
            print("0 - Retorna")
            try:
                opcao = self.pega_numero(0, 4)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
