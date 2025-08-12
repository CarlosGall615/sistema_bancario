from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao): #(conta: Conta, transacao: Transacao)
        transacao.registrar(conta)

    def adicionar_conta(self, conta): # (conta: Conta)
        self.contas.append(conta)


class PessoaFisica(Cliente):

    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)

        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class PessoaJuridica(Cliente):
    
    def __init__(self, endereco, cnpj, razao_social, nome_fantasia, inscricao_estadual):
        super().__init__(endereco)

        self.cnpj = cnpj
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.inscricao_estadual = inscricao_estadual


class Transacao(ABC):

    def registrar(self,): # (conta: Conta)
        pass


class Deposito(Transacao):

    def __init__(self, valor):
        super().__init__()
        self.valor = valor


class Saque(Transacao):

    def __init__(self, valor):
        super().__init__()
        self.valor = valor

      
class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        pass
    
    @classmethod
    def nova_conta(cls, cliente, numero): # (cliente: Cliente, numero: int) : Conta
        return cls(cliente, numero)
    # mapear selfs com @property
    def sacar(self, valor):
        pass
    #incluir funções existentes v02
    def depositar(self, valor):
        pass
    #incluir funções existentes v02

class ContaCorrente(Conta):

    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self._limite = 500.00
        self._limite_saques = 3


class Historico:

    def adicionar_transacao(): # (transacao: Transacao)
        pass