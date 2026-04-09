import pyodbc
import time
from abc import ABC, abstractmethod

server = 'TBS0676757W11-1\\SQLEXPRESS'
database = 'biblioteca_python'
username = 'conection_nicky'
password = 'NickyM469'

time.sleep(1) 

connection_string = f"""
DRIVER={{ODBC Driver 18 for SQL Server}};
SERVER={server};
DATABASE={database};
UID={username};
PWD={password};
TrustServerCertificate=yes;
"""


try:
    conn = pyodbc.connect(connection_string)
    print("Conexão bem-sucedida!")
except pyodbc.Error as e:
    print("Erro na conexão:")
    for err in e.args:
        print(err)
finally:
    try:
        conn.close()
    except:
        pass

#--------------------------------------------------------------------
# CLASSE BIBLIOTECA
class Biblioteca:
    MAX_LIVROS_POR_USUARIO = 5
    MULTA_DIARIA = 2.0
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#CLASSE LIVRO
class Livro:
    livros_emprestados = 0

    def __init__(self, __titulo, __autor):
        self.__titulo = __titulo
        self.__autor = __autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso!")
            Livro.livros_emprestados += 1
        else:
            print("Livro já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            Livro.livros_emprestados -= 1
            print(f"Livro '{self.__titulo}' devolvido!")
        else:
            print("O livro já está disponível.")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE USUARIO
class Usuario:
    def __init__(self, __nome, __idade):
        self.__nome = __nome
        self.__idade = __idade
        self.livros_emprestados = 0
        pass

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def emprestar(self, livro):
        if self.livros_emprestados < Biblioteca.MAX_LIVROS_POR_USUARIO:
            if livro.disponivel:
                livro.emprestar()
                self.livros_emprestados += 1
            else:
                print("Livro indisponível")

    def devolver(self, livro):
        if self.livros_emprestados > 0:
            livro.devolver()
            self.livros_emprestados -= 1
        else:
            print("Nenhum livro para devolver.")

    def apresentar(self):
        print(f"Nome: {self.__nome} e possui {self.__idade} anos.")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE PAGAMENTO
class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE FUNCIONARIO
class Funcionario(Pagamento, ABC):
    def __init__(self, __nome, __salario):
        self.__nome = __nome
        self.__salario = __salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario
    
    @abstractmethod
    def calcular_bonus(self):
        pass

    def mostrar_dados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')

    def processar_pagamento(self, valor):
        pass
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE BIBLIOTECARIO
class Bibliotecario(Funcionario):
    def __init__(self, __nome, __salario):
        super().__init__(__nome, __salario)

    def calcular_bonus(self):   
        return self.get_salario() * 0.10
    
    def mostrar_dados(self):
        print(f'Nome: {self.get_nome()}')
        print(f'Salário: {self.get_salario()}')

    def processar_pagamento(self, valor):
        print(f"Bibliotecário recebeu pagamento de R$ {valor:.2f}")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE GERENTE
class Gerente(Funcionario):
    def __init__(self, __nome, __salario):
        super().__init__(__nome, __salario)

    def calcular_bonus(self):
        return self.get_salario() * 0.20
    
    def mostrar_dados(self):
        print(f'Nome: {self.get_nome()}')
        print(f'Salário: {self.get_salario()}')

    def processar_pagamento(self, valor):
        print(f"Gerente recebeu pagamento de R$ {valor:.2f}")
#-----------------------------------------------------------------