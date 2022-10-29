

class TelaCandidato:

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!", 4: "A seguir, digite os novos dados"}
        print(opcoes[tipo_mensagem])

    def mostra_erro(self, erro):
        print(erro)

    def pega_numero(self, lim_inf, lim_sup):
        num = int(input("Digite uma das opções:"))
        if lim_inf <= num <= lim_sup:
            return num
        else:
            raise ValueError

    def pega_numero_candidato(self):
        while True:
            numero = input("Digite o número do candidato:")
            if len(numero) == 2 and 0 < int(numero) < 99:
                return numero
            else:
                print("Número inválido, tente novamente")

    def pega_cpf(self):
        while True:
            cpf = input("Digite o CPF:")
            if len(cpf) == 11:
                return cpf
            else:
                print("CPF inválido, tente novamente")

    def pega_dados_candidato(self):
        nome_candidato = input("Digite o nome:")
        cpf_candidato = self.pega_cpf()
        tipo_do_eleitor = input("Digite o tipo do eleitor:")
        numero_candidato = self.pega_numero_candidato()
        chapa_candidato = input("Digite a chapa do candidato:")
        cargo_candidato = input("Digite o cargo do candidato:")
        dados = {1: nome_candidato, 2: cpf_candidato, 3: tipo_do_eleitor, 4: numero_candidato,
                 5: chapa_candidato, 6: cargo_candidato}
        return dados

    def mostra_candidatos(self, dados_candidatos):
        if len(dados_candidatos) == 0:
            print("Nenhum candidato cadastrado!")
        else:
            print("Candidatos cadastrados:")
            contador = 0
            for dado in dados_candidatos:
                contador += 1
                if contador % 6 == 1:
                    print("Nome: " + dado)
                elif contador % 6 == 2:
                    print("CPF: " + dado)
                elif contador % 6 == 3:
                    print("Tipo de Eleitor: " + dado)
                elif contador % 6 == 4:
                    print("Número: " + dado)
                elif contador % 6 == 5:
                    print("Chapa: " + dado)
                else:
                    print("Cargo: " + dado)
                    print()

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Candidatos")
            print("#" * 20)
            print("1 - Cadastro de Candidato")
            print("2 - Exclusão de Candidato")
            print("3 - Alteração de Candidato")
            print("4 - Listagem dos Candidatos")
            print("0 - Retorna")
            try:
                opcao = self.pega_numero(0, 4)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
