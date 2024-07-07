class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f'Depósito: +R${valor:.2f}')
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print('Erro: O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f'Saque: -R${valor:.2f}')
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Erro: Saldo insuficiente.')

    def ver_extrato(self):
        print(f'Extrato da conta {self.numero_conta} - Titular: {self.nome_titular}')
        for item in self.extrato:
            print(item)
        print(f'Saldo atual: R${self.saldo:.2f}')



def menu_principal(conta):
    while True:
        print("\n### Menu Principal ###")
        print("1. Visualizar Extrato")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")
        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == '1':
            conta.ver_extrato()
        elif opcao == '2':
            valor_deposito = float(input("Digite o valor a depositar: "))
            conta.depositar(valor_deposito)
        elif opcao == '3':
            valor_saque = float(input("Digite o valor a sacar: "))
            conta.sacar(valor_saque)
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha uma opção válida (1/2/3/4).")


if __name__ == "__main__":
    numero_conta = input("Digite o número da conta: ")
    nome_titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))

    conta1 = ContaBancaria(numero_conta, nome_titular, saldo_inicial)

    menu_principal(conta1)
