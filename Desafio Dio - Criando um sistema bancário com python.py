menu = """
Olá! Bem-vindo(a) ao Banco Rigel. Digite a opção desejada: 
[d] Depósito
[s] Saque
[e] extrato
[r] sair

"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do Depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!")

        else:
            print("Não foi possível realizar o depósito. O valor informado é inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saque = numero_saques >= LIMITE_DIARIO_SAQUES

        if excedeu_saldo:
            print("Transação não aprovada. Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação não permitida: Valor solicitado excede o limite de saque.")

        elif excedeu_saque:
            print("Operação não permitida: o número máximo de saques por dia foi atingido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque efetuado com sucesso! Por favor, retire seu dinheiro.")

        else:
            print("Não foi possível realizar a operação. O valor informado é inválido.")

    elif opcao == "e":
        print("\n===============*** EXTRATO ***===============")
        print("Seu extrato está vazio. Nenhuma movimentação foi realizada ainda." if not extrato else extrato)
        print(f"\n Saldo total: R$ {saldo:.2f}")
        print("=====================******=====================")

    elif opcao == "r":
        break

    else:
        print("Opção inválida. Verifique os dados e tente novamente.")
