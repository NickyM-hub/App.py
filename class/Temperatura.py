class controleTemperatura:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def atualizarTemperatura(self):
        if (self.__temperatura > -50 and self.__temperatura < 100):
            print('Temperatura aceita')
        else:
            print('"Temperatura inválida! Deve estar entre -50 e 100 graus Celsius')