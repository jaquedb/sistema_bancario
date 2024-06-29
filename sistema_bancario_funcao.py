menu = """
====MENU====
[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
===========
"""

saldo = 0
extrato_1 = ""
numero_saques = 1
LIMITE_SAQUE = 3


def deposito ():
    global saldo
    global extrato_1
    valor = float(input("Informe o valor do depósito "))
    if valor > 0:
        extrato_1 += f" Depósito: R$ {valor:.2f}\n"
        saldo += valor
        print ()
        print (f" Depósito: {valor:.2f} \n Saldo atual: R$ {saldo:.2f} ")
    else:
        print ("Informe um valor válido") 


def saque ():
    limite = 500
    global saldo
    global extrato_1
    global numero_saques
    global LIMITE_SAQUE
    valor = float(input("Informe o valor do saque "))
    if valor > limite:
        print ()
        print ("Não foi possivel realizar a operação. O valor excede o limite por saque")
    elif valor > saldo:
        print ()
        print ("Não foi possível realizar a operação. Você nao tem saldo suficiente")
    elif valor <= saldo:
        extrato_1 += f" Saque: R$ {valor:.2f} \n"
        saldo -= valor
        numero_saques += 1
        print ()
        print (f" Saque: R$ {valor:.2f} \n Saldo atual: R$ {saldo:.2f} ")


def extrato ():
    print (extrato_1)
    print (f" Saldo atual: R$ {saldo:.2f}")



while True:
    print (menu)
    opcao = int(input("Digite uma opção "))
    if opcao == 1:
        deposito ()

    elif  opcao == 2:
        if numero_saques > LIMITE_SAQUE:
            print ("Limite de saque diário excedido")
            continue
        saque ()

    elif opcao == 3:
        if not extrato_1:
            print ()
            print ("===========EXTRATO=========== \n")
            print ("Nenhuma transação foi realizada \n")
            print ("==============================")
        else:
            print ()
            print  ("===========EXTRATO=========== \n")
            extrato ()
            print ()
            print ("=============================")

    elif opcao == 0:
        print ("Obrigado(a) por usar nosso sistema! ")
        break

    elif opcao >= 4:
        print ("Digite uma opção válida")