
# Desafio Otimizando o Sistema Bancário com Funções Pyhton

# Neste desafio foi proposto otimizar a v01 do sistema bancário ajustando funções para
# depoisitar, sacar, exibir extrado, cadastrar usuário, criar uma conta

# Esta é a v02 do Desafio, seguem as opções aprimoradas:

# * Todo o Sistema com Funções específicas
# * Cadastro de Usuário
#   - Um (1) Usuário por CPF
#   - Múltiplas contas por Usuário
# * Criar contas:
#   - Conta Corrente
#   - Conta Poupança
# * Lista de Contas:
#   - Conta Corrente
#   - Conta Poupança


def menu():
    menu = """ 
=============== MENU ===============

        [1] - Criar Usuário

        [2] - Criar Conta Corrente
        [3] - Criar Conta Poupança

        [4] - Depositar
        [5] - Sacar
        [6] - Extrato

        [7] - Exibir Contas

        [0] - Sair
"""
    return input(menu)

def menu_contas():
    menu_contas = """ 
=============== CONTAS ===============

        [1] - Conta Pessoal
        [2] - Conta Empresarial
"""
    return input(menu_contas)

def depositar(saldo, valor_deposito, extrato, /):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: {'R$':>21} {valor_deposito:.2f}\n"

    else:
        print(f"A Operação Falhou, Digite os Dados Corretamente.")

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, VALOR_LIMITE_SAQUE_DIARIO, LIMITE_SAQUES, saques_efetuados):

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

    return saldo, extrato

def exibir_extrato(saldo, linha_extrato, /, *, extrato):
    print("=============== EXTRATO ===============")
    print(f"{'Tipo':<15} {'Valor':>23}")
    print(linha_extrato.center(37, "-"))
    print("Nehuma Movimentação Encontrada." if not extrato else extrato)
    print(linha_extrato.center(37, "-"))
    print(f"\nSaldo: {'R$':>24} {saldo:.2f}")
    print("=======================================")
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = int(input("Informe o número do CPF(somente números): "))

    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            print("\n Usuário já Cadastrado! Tente Novamente.")
            return
    
    nome = input("Insara o Nome Completo: ")
    endereco = input("Informe o Endereço  (Logadouro - Nº - Bairro - Cidade/Sigla Estado): ")
    data_nascimento = input("Informa a Data de Nascimento (dd-mm-aaa): ")
    telefone = input("Insira o Número do Telefone com DDD(somente números): ")

    novo_usuario = {
        "CPF": cpf, 
        "Nome": nome, 
        "Endereço": endereco, 
        "Data de Nascimento": data_nascimento,
        "Telefone": telefone}
    
    usuarios.append(novo_usuario)
    
    print("\nSeu Cadastro foi Concluído com Sucesso!\n\nPara Continuar, Crie sua Conta.")

    return novo_usuario
    
def criar_conta_corrente(agencia, numero_conta, usuario):
    
    conta = {
        "Agencia": agencia,
        "Número da Conta": numero_conta,
        "Usuário": usuario
    }
    print("\nConta Corrente Criada com Sucesso!")
    return conta
    
def criar_conta_poupanca(agencia, numero_conta, usuario):

    conta = {
        "Agencia": agencia,
        "Número da Conta": numero_conta,
        "Usuário": usuario
    }
    print("\nConta Poupança Criada com Sucesso!")
    return conta

def listar_contas(contas, linha_extrato):
    for conta in contas:
        lista_de_contas = f"""
            Agência: {conta['Agencia']}
            Conta: {conta['Número da Conta']}
            Titular: {conta['Usuário']['Nome']}
        """
        print(linha_extrato.center(37, "-"))
        print(lista_de_contas)

def main():
    saldo = 0
    saques_efetuados = 0
    extrato = ""

    linha_extrato = "-"

    usuarios = []
    conta_corrente = []
    conta_poupanca = []
    numero_conta = 1
    AGENCIA = "0001"
    

    LIMITE_SAQUES = 3
    VALOR_LIMITE_SAQUE_DIARIO = 500

    while True:
        opcao = menu()

        # Inicio Opção [1] ---- >>>> Cadastrar Usuário
        if opcao == "1":
            usuario = criar_usuario(usuarios)

            if usuario:
                option = menu_contas()

                if option == "1":
                    conta = criar_conta_corrente(AGENCIA, numero_conta, usuario)

                    if conta:
                        conta_corrente.append(conta)
                        numero_conta += 1

                elif option == "2":
                    conta = criar_conta_poupanca(AGENCIA, numero_conta, usuario)

                    if conta:
                        conta_poupanca.append(conta)
                        numero_conta += 1

        # Inicio Opção [2] ---- >>>> Criar Conta Corrente
        elif opcao == "2":
            cpf = int(input("Informe o número do CPF(somente números): "))

            for usuario in usuarios:
                if usuario["CPF"] == cpf:
                    conta = criar_conta_corrente(AGENCIA, numero_conta, usuario)

                    if conta:
                        conta_corrente.append(conta)
                        numero_conta += 1
                else:
                    print("\nUsuário nao Encontrado, Cadastre-se para Criar uma Conta Corrente")
                
        # Inicio Opção [3] ---- >>>> Criar Conta Poupança
        elif opcao == "3":
            cpf = int(input("Informe o número do CPF(somente números): "))

            for usuario in usuarios:
                if usuario["CPF"] == cpf:
                    conta = criar_conta_poupanca(AGENCIA, numero_conta, usuario)

                    if conta:
                        conta_poupanca.append(conta)
                        numero_conta += 1
                else:
                    print("\nUsuário nao Encontrado, Cadastre-se para Criar uma Conta Poupança.")
                
        # Inicio Opção [4] ---- >>>> Depositar Dinheiro
        elif opcao == "4":
            valor_deposito = float(input("Valor a Depositar: R$ "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        # Inicio Opção [5] ---- >>>> Sacar Dinheiro
        elif opcao == "5":
            valor_saque = float(input("Valor a Sacar: R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor_saque=valor_saque,
                extrato=extrato,
                VALOR_LIMITE_SAQUE_DIARIO=VALOR_LIMITE_SAQUE_DIARIO,
                LIMITE_SAQUES=LIMITE_SAQUES,
                saques_efetuados=saques_efetuados)

        # Inicio Opção [6] ---- >>>> Exibir Extrato Movimentações
        elif opcao == "6":

            saldo, extrato = exibir_extrato(saldo, linha_extrato, extrato=extrato)

        # Inicio Opção [7] ---- >>>> Exibir Contas Cadastradas
        elif opcao == "7":

            tipo = input("\n[1] - Ver Contas Corrente\n[2] - Ver Contas Poupança\nEscolha: ")
            
            if tipo == "1":
                listar_contas(conta_corrente, linha_extrato)
            elif tipo == "2":
                listar_contas(conta_poupanca, linha_extrato)
            else:
                print("Opção Inválida.")

        # Inicio Opção [8] ---- >>>> Sair do Sistema
        elif opcao == "0":

            print("Obrigado por utilizar nosso sistema. Volte Sempre!\n")
            break
        
        # Inicio Opção [2] ---- >>>> Mensagem Opções Inválidas
        else:
            print("A Operação Falhou, por favor escolha uma Opção Válida. ")

    return
main()