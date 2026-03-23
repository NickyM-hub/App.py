class ContaBancaria:
    def __init__(self, nome, __saldo):
        self.nome = nome
        self.__saldo = __saldo
        pass

    def depositar(self, valor):
        if valor > 0:
            print("Valor depositado com sucesso")
            self.__saldo += valor
            return self.__saldo
        else:
            print("Não foi possível depositar o valor desejado")
    
    def sacar(self, valor):
        if valor < self.__saldo:
            self.__saldo -= valor
            print("Valor sacado com sucesso")
            return self.__saldo
        else:
            print("Saldo indísponível")
    
    def ver_saldo(self):
        print(f"O usuário {self.nome} tem: R${self.__saldo} reais na conta bancária")
        return self.__saldo
    
conta = ContaBancaria("Nicole", 1200)

conta.sacar(600)
conta.ver_saldo()
conta.depositar(800)
conta.ver_saldo()
