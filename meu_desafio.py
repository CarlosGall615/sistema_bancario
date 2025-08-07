class ContaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):

        print(f"{self.titular}, seu Saldo é de: R$ {self.saldo}")
        return self.saldo
    
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

        nome = input("Digite seu nome: ")
        saldo_inicial = float(input("Digite o Saldo inicial(R$): "))

        nova_conta = ContaBancaria(nome, saldo_inicial)
        print(f"\nBem-Vindo {nome}, Sua conta foi criada com Sucesso.\n")
        
        return self.contas_cadastradas.append(nova_conta)
    
    def listar_contas(self):

        if not self.contas_cadastradas:
            print("Não encontramos Contas Cadastradas ate o Momento.")
        
        for conta in self.contas_cadastradas:
            print(f"\t__________ CONTAS __________\n")
            print(f"\tNome:\t\t{conta.titular}")
            print(f"\tSaldo:\t\tR$ {conta.saldo:.2f}\n")
            print(f"\t____________________________\n")

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

        elif option == "0":
            print("Obrigado por Usar o Sistema!")
            break

main()