

class TelaCargo:

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

    def pega_nome_cargo(self):
        while True:
            nome_cargo = input("Digite o nome do Cargo:")
            if len(nome_cargo) > 0:
                return nome_cargo
            else:
                print("Nome inválido, tente novamente")

    def altera_nome_cargo(self):
        while True:
            nome_cargo = input("Digite o novo nome do Cargo:")
            if len(nome_cargo) > 0:
                return nome_cargo
            else:
                print("Nome inválido, tente novamente")

    def mostra_cargos(self, cargos):
        if len(cargos) > 0:
            print("Cargos cadastrados:")
            for nome_cargo in cargos:
                print(nome_cargo)
        else:
            print("Nenhum cargo cadastrado")

    def mostra_candidatos_cargo(self, lista_candidatos, nome_cargo):
        if len(lista_candidatos) == 0:
            print("Nenhum candidato cadastrado")
        else:
            print("Candidatos ao Cargo de " + nome_cargo)
            for candidato in lista_candidatos:
                print(candidato)

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Cargos")
            print("#" * 20)
            print("1 - Cadastro de Cargo")
            print("2 - Exclusão de Cargo")
            print("3 - Alteração de Cargo")
            print("4 - Listagem de Cargos")
            print("5 - Listagem de Candidatos por Cargo")
            print("0 - Retornar")
            try:
                opcao = self.pega_numero(0, 5)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
