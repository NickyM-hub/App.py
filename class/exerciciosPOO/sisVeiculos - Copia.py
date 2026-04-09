class Veiculo: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        pass

    def mover(self):
        print(f"O {self.modelo}, do modelo: {self.modelo}, está em movimento")

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def abrir_porta_malas(self):
        print("Abrindo porta-malas")

class Moto(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def empinar(self):
        print("Empinando moto")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        
    def carregar_carga(self):
        print("Carregando carga")