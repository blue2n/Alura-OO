

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Contruindo objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def estrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__aldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor