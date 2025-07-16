saldo = 0
saques_efetuados = 0
extrato = ""

linha_extrato = "-"

LIMITE_SAQUES = 3
VALOR_LIMITE_SAQUE_DIARIO = 500

menu = """ 
=============== MENU ===============

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [0] - Sair

_____________________________________
"""

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Valor a Depositar: R$ "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: {'R$':>21} {valor_deposito:.2f}\n"

        else:
            print(f"A Operação Falhou, Digite os Dados Corretamente.")

    elif opcao == "2":
        valor_saque = float(input("Valor a Sacar: R$ "))

        exedeu_saldo = valor_saque > saldo

        excedeu_valor_limite = valor_saque > VALOR_LIMITE_SAQUE_DIARIO

        excedeu_quantidades_saque = saques_efetuados >= LIMITE_SAQUES

        if exedeu_saldo:
            print("Seu Saldo é Insuficiente.")
        
        elif excedeu_valor_limite:
            print(f"Seu limite de Saque é de: {VALOR_LIMITE_SAQUE_DIARIO:.2f}")

        elif excedeu_quantidades_saque:
            print("Número de Saques Excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: {'R$':>24} {valor_saque:.2f}\n"
            saques_efetuados += 1
        else:
            print(f"A Operação Falhou, Digite os Dados Corretamente.")
       

    elif opcao == "3":
        print("=============== EXTRATO ===============")
        print(f"{'Tipo':<15} {'Valor':>23}")
        print(linha_extrato.center(37, "-"))
        print("Nehuma Movimentação Encontrada." if not extrato else extrato)
        print(linha_extrato.center(37, "-"))
        print(f"\nSaldo: {'R$':>24} {saldo:.2f}")
        print("=======================================")

    elif opcao == "0":
        print("Obrigado por utilizar nosso sistema. Volte Sempre!\n")
        break

    else:
        print("A Operação Falhou, por favor escolha uma Opção Válida. ")


