menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
qtd_saques = 0
qtd_max_saques = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
            
        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Saldo insuficiente")

        elif valor > limite:
            print("Operação falhou! Valor ultrapassa o limite permitido para saque")

        elif qtd_saques >= qtd_max_saques:
            print("Operação falhou! Você ultrapassou o limite de saques diarios permitido")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
            qtd_saques +=1

        else:
            print("Operação inválida! O valor informado é invalido")
        
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == 0:
        break

    else:
        print("Operação falhou, informe novamente a operação desejada")