from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, __nome, __salario):
        self.__nome = __nome
        self.__salario = __salario

    @abstractmethod
    def calcularBonus(self):
        pass

    def mostrarDados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')


class Bibliotecario(Funcionario):
    def __init__(self, __nome, __salario):
        super().__init__(__nome, __salario)

    def calcularBonus(self):
        self.__salario * 0,2
        return self.__salario
    
    def mostrarDados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')


class Gerente(Funcionario):
    def __init__(self, __nome, __salario):
        super().__init__(__nome, __salario)

    def calcularBonus(self):
        self.__salario * 0,4
        return self.__salario
    
    def mostrarDados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')