class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular 
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Seu saldo é de {}".format(self.saldo))

    def saca(self, valor):
        if (valor <= self.__saldo + self.__limite):
            self.__saldo -= valor 
        else: 
            print('O valor {} passou o limite'.format(valor))
            
    def deposita(self, valor):
        self.__saldo += valor 

    def transfere(self, valor, destinatario):
        self.saca(valor)
        destinatario.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def titular(self):
        return self.__titular
    
    @limite.setter 
    def limite(self, limite):
        self.__limite = limite


    

    

