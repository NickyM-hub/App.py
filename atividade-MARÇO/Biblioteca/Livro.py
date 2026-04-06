class Livro:
    def __init__(self, __titulo, __autor, disponivel):
        self.__titulo = __titulo
        self.__autor = __autor
        self.disponivel = disponivel
        pass

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("Livro já está emprestado.")

    def devolver(self):
        self.disponivel = True
        print("Livro devolvido com sucesso!")


class Usuario:
    def __init__(self, __nome, __idade):
        self.__nome = __nome
        self.__idade = __idade
        pass

    def apresentar(self):
        print(f"Nome: {self.nome} e possui {self.idade} anos.")