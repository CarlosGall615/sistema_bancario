class ContaBancaria:
    contador_contas = 1

    def __init__(self, cpf, titular, saldo=0):
        self.cpf = cpf
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = ContaBancaria.contador_contas
        ContaBancaria.contador_contas += 1
        self.AGENCIA = "0001"

    #def exibir_conta(self):

        #print(f"{self.titular}, sua Conta é {self.numero_conta} e seu Saldo é de: R$ {self.saldo}")
        #return self.saldo
    
    def depositar(self, valor):

        self.saldo += valor
        print(f"Depósito de R${valor} efetuado com Sucesso!")
    
    def sacar(self, valor):

        if valor > self.saldo:
            print("Saldo Indisponível no Momento. Verifique seu Saldo.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} efetuado com Sucesso!")

class SistemaBancario:

    def __init__(self):
        self.contas_cadastradas = []

    def abrir_conta(self):

        cpf = input("Digite o CPF(somente números): ")
        nome = input("Digite seu nome: ")
        saldo_inicial = float(input("Digite o Saldo inicial(R$): "))
        
        nova_conta = ContaBancaria(cpf, nome, saldo_inicial)
        print(f"\nBem-Vindo {nome}, Sua conta foi criada com Sucesso.\n")

        return self.contas_cadastradas.append(nova_conta)
    
    def listar_contas(self):

        if not self.contas_cadastradas:
            print("Não encontramos Contas Cadastradas ate o Momento.")
        
        for conta in self.contas_cadastradas:
            print(f"\t__________ CONTAS __________\n")
            print(f"\tNome:\t\t{conta.titular}")
            print(f"\tAgência:\t{conta.AGENCIA}")
            print(f"\tConta:\t\t{conta.numero_conta}")
            print(f"\tCPF:\t\t{conta.cpf}")
            print(f"\tSaldo:\t\tR$ {conta.saldo:.2f}\n")
            
    
    def buscar_cliente(self, cpf):

        for conta in self.contas_cadastradas:
            if conta.cpf == cpf:
                return conta
        return None   

    def buscar_conta_cliente(self, numero_conta):

        for conta in self.contas_cadastradas:
            print(conta.numero_conta)
            
    

        
    def depositar(self):

        cpf = input("CPF: ")
        conta = self.buscar_cliente(cpf)

        if conta:
            
            print(f"Nº da Conta: {conta.numero_conta}")
            conta_para_deposito = input("Digite a Conta para Depósito: ")
            if conta.numero_conta == conta_para_deposito:
                valor = float(input("Digite o Valor para Depositar: "))
                print(f"Depósito de R$ {valor:.2f} Efetuado com Sucesso na Conta {conta_para_deposito}. ")
            
                
                conta.depositar(valor)
            
    def sacar(self):

        cpf = input("CPF: ")
        conta = self.buscar_cliente(cpf)

        if conta:
            valor = float(input("Digite o Valor para Saque: "))
            conta.sacar(valor)

    def transacao(self):
        pass


def menu():

    menu = """
========== BEM-VINDO ==========
                                |
        Escolha uma Opção:      |
                                |
    [1] - Criar uma Conta       |
    [2] - Listar Contas         |
    [3] - Depositar             |
    [4] - Sacar                 |
    [5] - Extrato               |
                                |
    [0] - Sair                  |
"""
    return input(menu)

def main():

    sistema = SistemaBancario()
    

    while True:

        option = menu()

        if option == "1":
            sistema.abrir_conta()

        elif option == "2":
            sistema.listar_contas()
        
        elif option == "3":
            sistema.depositar()

        elif option == "4":
            sistema.sacar()

        elif option == "5":
            sistema.transacao()

        elif option == "0":
            print("Obrigado por Usar o Sistema!")
            break

main()