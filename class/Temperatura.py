class ControleTemperatura:
    def __init__(self, temperatura):
        self.__temperatura = temperatura
        pass

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def atualizarTemperatura(self, valor):
        if -50 <= valor <= 100:
            self.__temperatura = valor
            print('Temperatura aceita')
        else:
            print('"Temperatura inválida! Deve estar entre -50 e 100 graus Celsius')

    def converter_para_fahrenheit (self):
        return self.__temperatura * 1.8 + 32

# teste
temp = ControleTemperatura(25)
print("Temperatura atual:", temp.atualizarTemperatura)
temp.atualizarTemperatura = 30
print("Nova temperatura:", temp.atualizarTemperatura)
temp.atualizarTemperatura = 150  # deve mostrar erro
print("Em Fahrenheit:", temp.converter_para_fahrenheit())