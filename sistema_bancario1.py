menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input("Informe a operação que deseja realizar" + menu))
    if opcao == 1:
        valor = float(input("Informe o valor que deseja depósitar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido.")
    elif opcao == 2:
        valor = float(input("Informe o valor que deseja sacar: "))
        if valor>saldo:
            print("Você não tem saldo suficiente.")
        elif valor>limite:
            print("O valor do saque excede o limite.")
        elif numero_saques>=LIMITE_SAQUES:
            print("Limite de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1
        else:
            print("O valor informado é inválido.")
    elif opcao == 3:
        print("EXTRATO ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print()
    elif opcao == 0:
        break
    else:
        print("Por favor, selecione uma operação válida.")