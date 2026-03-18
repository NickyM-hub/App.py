from abc import ABC, abstractmethod

class Midia(ABC):
    @abstractmethod
    def exibir_info(self):
        pass

class Livro:
    def __init__(self, titulo, autor, numero_pg):
        self.titulo = titulo
        self.autor = autor
        self.numero_pg = numero_pg
        pass

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.numero_pg}")
        print("-" * 30)

class Filme:
    def __init__(self, titulo, diretor, duracao):
        self.titulo = titulo
        self.diretor = diretor
        self.duracao = duracao
        pass

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.diretor}")
        print(f"Duração do filme: {self.duracao}") # duração em minutos
        print("-" * 30)

class Musica:
    def __init__(self, titulo, artista, duracaoS):
        self.titulo = titulo
        self.artista = artista
        self.duracaoS = duracaoS # duração em segundos
        pass

    def exibir_info(self):
        print(f"Título: {self.titulo}")
        print(f"Diretor: {self.artista}")
        print(f"Duração da música: {self.duracaoS} segundos")
        print("-" * 30)

midias = [
    Livro("Dom Casmurro", "Machado de Assis", 256),
    Filme("Inception", "Christopher Nolan", 148),
    Musica("Bohemian Rhapsody", "Queen", 354)
]

for midia in midias:
    midia.exibir_info()