from abc import ABC, abstractmethod

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

    def emprestar_livro(self, livro):
        if self.livros_emprestados < Biblioteca.MAX_LIVROS_POR_USUARIO:
            if livro.disponivel:
                livro.emprestar()
                self.livros_emprestados += 1
            else:
                print("Livro indisponível")

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

    @abstractmethod
    def calcularBonus(self):
        pass

    def mostrarDados(self):
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

    def calcularBonus(self):
        
        return self._Funcionario__salario * 0.10
    
    def mostrarDados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')

    def processar_pagamento(self, valor):
        print(f"Bibliotecário recebeu pagamento de R$ {valor:.2f}")
#-----------------------------------------------------------------

#-----------------------------------------------------------------
#CLASSE GERENTE
class Gerente(Funcionario):
    def __init__(self, __nome, __salario):
        super().__init__(__nome, __salario)

    def calcularBonus(self):
        self.__salario * 0.20
        return self.__salario
    
    def mostrarDados(self):
        print(f'Nome: {self.__nome}')
        print(f'Salário: {self.__salario}')

    def processar_pagamento(self, valor):
        print(f"Gerente recebeu pagamento de R$ {valor:.2f}")
#-----------------------------------------------------------------

# =========================
# TESTE DO SISTEMA
# =========================
if __name__ == "__main__":
    # Livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis")
    livro2 = Livro("1984", "George Orwell")

    # Usuário
    user = Usuario("João", 20)
    user.apresentar()

    # Empréstimos
    user.emprestar_livro(livro1)
    user.emprestar_livro(livro1)  # erro (já emprestado)
    user.emprestar_livro(livro2)

    print("Total emprestados:", Livro.total_livros_emprestados)

    # Devolução
    user.devolver_livro(livro1)
    print("Total emprestados:", Livro.total_livros_emprestados)

    # Funcionários
    b = Bibliotecario("Ana", 3000)
    g = Gerente("Carlos", 5000)

    b.mostrar_dados()
    print("Bônus:", b.calcular_bonus())
    b.processar_pagamento(3000)

    print()

    g.mostrar_dados()
    print("Bônus:", g.calcular_bonus())
    g.processar_pagamento(5000)