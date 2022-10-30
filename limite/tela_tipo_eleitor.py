from limite.tela import Tela


class TelaTipoEleitor(Tela):

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!"}
        print(opcoes[tipo_mensagem])

    def pega_nome_tipo_eleitor(self):
        while True:
            nome_tipo_eleitor = input("Digite o nome do Tipo de Eleitor:")
            if len(nome_tipo_eleitor) > 0:
                return nome_tipo_eleitor
            else:
                print("Nome inválido, tente novamente")

    def altera_nome_tipo_eleitor(self):
        while True:
            nome_tipo_eleitor = input("Digite o novo nome do Tipo de Eleitor:")
            if len(nome_tipo_eleitor) > 0:
                return nome_tipo_eleitor
            else:
                print("Nome inválido, tente novamente")

    def mostra_tipos_eleitor(self, tipos_eleitor):
        if len(tipos_eleitor) > 0:
            print("Tipos de Eleitor cadastrados:")
            for nome_tipo_eleitor in tipos_eleitor:
                print(nome_tipo_eleitor)
        else:
            print("Nenhum Tipo de Eleitor cadastrado")

    def mostra_eleitores_tipo_eleitor(self, lista_eleitores, nome_tipo_eleitor):
        if len(lista_eleitores) == 0:
            print("Nenhum eleitor cadastrado")
        else:
            print("Eleitores com o tipo " + nome_tipo_eleitor)
            for eleitor in lista_eleitores:
                print(eleitor)

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Tipos de Eleitor")
            print("#" * 20)
            print("1 - Cadastro de Tipo de Eleitor")
            print("2 - Exclusão de Tipo de Eleitor")
            print("3 - Alteração de Tipo de Eleitor")
            print("4 - Listagem de Tipos de Eleitor")
            print("5 - Listagem de Eleitores por Tipo")
            print("0 - Retornar")
            try:
                opcao = self.pega_numero(0, 5)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
