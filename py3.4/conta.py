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

    def __pode_sacar(self, saldo_disponivel):
        saldo_conta = self.__saldo + self.__limite
        return saldo_disponivel <= saldo_conta
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('Saldo insuficiente')

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property   
    def saldo(self):
        return self.__saldo
    
    @property
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return '001'
    
    @staticmethod
    def codigos_bancos():
        return {'BB' : '001', 'Caixa' : '104', 'Bradesco' : '273'}
