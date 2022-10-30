from limite.tela import Tela


class TelaUrna(Tela):

    def mensagem(self, tipo_mensagem: int):
        opcoes = {1: "Cadastro realizado com sucesso!", 2: "Cadastro excluído com sucesso!",
                  3: "Cadastro alterado com sucesso!", 4: "A seguir, digite os novos dados",
                  5: "Urna homologada com sucesso!", 6: "Candidato inválido!",
                  7: "Votos realizados com sucesso!", 8: "Votação encerrada!"}
        print(opcoes[tipo_mensagem])

    def pega_numero_voto(self, cargo):
        while True:
            print("Digite o número do candidato para o cargo de " + cargo)
            numero = input()
            if len(numero) == 2 and 0 <= int(numero) <= 99:
                return numero
            else:
                print("Número inválido, tente novamente")

    def confirma_voto(self, candidato):
        while True:
            print("Candidato escolhido: " + candidato)
            confirmacao = input("Deseja confirmar o voto? (S/N):")
            if confirmacao == "S":
                return True
            if confirmacao == "N":
                return False
            else:
                print("Resposta inválida")

    def pega_cpf(self):
        while True:
            cpf = input("Digite o CPF:")
            if len(cpf) == 11:
                return cpf
            else:
                print("CPF inválido, tente novamente")

    def pega_codigo_urna(self):
        while True:
            try:
                codigo = int(input("Digite o código da urna:"))
                return codigo
            except ValueError:
                print("Código inválido, tente novamente")

    def pega_dados_urna(self):
        while True:
            try:
                centro = input("Digite o centro da Urna:")
                turno = input("Digite o turno da eleição:")
                codigo = int(input("Digite o código da urna:"))
                if len(centro) > 0 and len(turno) > 0:
                    dados = {1: centro, 2: turno, 3: codigo}
                    return dados
                else:
                    print("Alguns dados inválidos, tente novamente")
            except ValueError:
                print("Código inválido, tente novamente")

    def mostra_urnas(self, dados_urnas):
        if len(dados_urnas) == 0:
            print("Nenhuma urna cadastrada!")
        else:
            print("Urnas cadastradas:")
            contador = 0
            for dado in dados_urnas:
                contador += 1
                if contador % 3 == 1:
                    print("Centro: " + dado)
                elif contador % 3 == 2:
                    print("Turno: " + dado)
                else:
                    print("Código: " + dado)
                    print()

    def mostra_resultado_urna(self, resultado, vencedor, cargo):
        print("Resultados para " + cargo)
        for candidato in resultado:
            print(candidato + ": " + str(resultado[candidato]))
        print("Vencedor na urna: " + vencedor)
        print()

    def mostra_opcoes(self):
        while True:
            print("#" * 20)
            print("Urnas")
            print("#" * 20)
            print("1 - Cadastro de Urnas")
            print("2 - Exclusão de Urnas")
            print("3 - Alteração de Urnas")
            print("4 - Listagem dos Urnas")
            print("5 - Acesso a Urna")
            print("0 - Retorna")
            try:
                opcao = self.pega_numero(0, 5)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")

    def mostra_opcoes_urna(self):
        while True:
            print("#" * 20)
            print("Funções da Urna")
            print("#" * 20)
            print("1 - Cadastro de Eleitores na Urna")
            print("2 - Exclusão de Eleitores da Urna")
            print("3 - Cadastro de Candidatos na Urna")
            print("4 - Exclusão de Candidatos da Urna")
            print("5 - Homologar a Urna")
            print("6 - Realizar Voto")
            print("7 - Apuração do Resultado da Urna")
            print("0 - Retorna")
            try:
                opcao = self.pega_numero(0, 7)
                return opcao
            except ValueError:
                print("Opção inválida, tente novamente")
