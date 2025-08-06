


class Conta:

    numero_conta = 1

    def __init__(self, numero, cliente):

        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def Saldo(self):
        pass

    def NovaConta(self, conta):
        self.conta = conta

    def Sacar(self):
        pass

    def Depositar(self):
        pass

class ContaCorrente(Conta):

    def __init__(self, limite, limite_saque):
        super().__init__()

        self.limite = limite
        self.limite_saque = limite_saque




class Historico:
    pass



class Transacao:
    pass


class Cliente:

    def __init__(self, endereco):

        self._endereco = endereco
        


    def realizar_transacao(self):
        pass

    def adicionar_conta(self):
        pass

class PessoaFisica(Cliente):

    def __init__(self, cpf, nome, data_nascimento):
        super().__init__()

        self.cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        

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
        [8] - Exibir Dados Cadastrados

        [0] - Sair
"""
    return input(menu)

def criar_usuario(usuarios):

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("\n Usuário já Cadastrado! Tente Novamente.")
            return
        
    cpf = input("Informe o número do CPF(somente números): ")
    nome = input("Insara o Nome Completo: ")
    endereco = input("Informe o Endereço  (Logadouro - Nº - Bairro - Cidade/UF): ")
    data_nascimento = input("Informa a Data de Nascimento (dd-mm-aaa): ")
    

    cliente = PessoaFisica(cpf, endereco, nome, data_nascimento)
    usuarios.append(cliente)
    
    print("\nSeu Cadastro foi Concluído com Sucesso!\n\nPara Continuar, Crie sua Conta.")

def criar_conta_corrente(agencia, numero_conta, usuarios):

    cpf = int(input("Informe o número do CPF(somente números): "))

    for usuario in usuarios:
        if usuario.cpf == cpf:
            
            conta = Conta.NovaConta(agencia, numero_conta, usuarios)
            conta.append(conta)

            if conta:
                numero_conta += 1
            else:
                print("\nUsuário nao Encontrado, Cadastre-se para Criar uma Conta Corrente")
    
    print("\nConta Corrente Criada com Sucesso!")
    return conta

def main():
    #saldo = 0
    #saques_efetuados = 0
    #extrato = ""

    #linha_extrato = "-"

    #usuarios = []
    #conta_corrente = []
    #conta_poupanca = []
    #numero_conta = 1
    #AGENCIA = "0001"
    

    #LIMITE_SAQUES = 3
    #VALOR_LIMITE_SAQUE_DIARIO = 500

    contas = []
    usuarios = []

    while True:
        opcao = menu()

        # Inicio Opção [1] ---- >>>> Cadastrar Usuário
        if opcao == "1":
            usuario = criar_usuario(usuarios)

        # Inicio Opção [2] ---- >>>> Criar Conta Corrente
        elif opcao == "2":
            conta = criar_conta_corrente(contas)
                
        # Inicio Opção [3] ---- >>>> Criar Conta Poupança
        elif opcao == "3":
            break
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
            break
            valor_deposito = float(input("Valor a Depositar: R$ "))

            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        # Inicio Opção [5] ---- >>>> Sacar Dinheiro
        elif opcao == "5":
            break

        # Inicio Opção [6] ---- >>>> Exibir Extrato Movimentações
        elif opcao == "6":
            break

        # Inicio Opção [7] ---- >>>> Exibir Contas Cadastradas
        elif opcao == "7":
            break
            tipo = input("\n[1] - Ver Contas Corrente\n[2] - Ver Contas Poupança\nEscolha: ")
            
            if tipo == "1":
                listar_contas(conta_corrente, linha_extrato)
            elif tipo == "2":
                listar_contas(conta_poupanca, linha_extrato)
            else:
                print("Opção Inválida.")

        # Inicio Opção [0] ---- >>>> Sair do Sistema
        elif opcao == "0":

            print("Obrigado por utilizar nosso sistema. Volte Sempre!\n")
            break
        
        # Inicio Opção [2] ---- >>>> Mensagem Opções Inválidas
        else:
            print("A Operação Falhou, por favor escolha uma Opção Válida. ")

    return
main()