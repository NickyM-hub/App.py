class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        pass

    def mostrar_dados(self):
        pass


class Gerente(Funcionarios):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        if self.bonus:
            self.salario += self.bonus
            return self.salario
        else:
            print("Não foi possível calcular o salário")
            
    def mostrar_dados(self):
        self.salario_total()
        print(f"Gerente {self.nome} possui um salário de: {self.salario} reais")
        print("-" * 30)


class Desenvolvedor(Funcionarios):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def programar(self):
        print(f"Dev está codando em: {self.linguagem}")
        print("-" * 30)

    def mostrar_dados(self):
        print(f"Dev {self.nome} possui um salário de: {self.salario} reais")
        print("-" * 30)


class Estagiario(Funcionarios):
    def __init__(self, nome, salario, carga_horaria):
        super().__init__(nome, salario)
        self.carga_horaria = carga_horaria

    def estudar(self):
        print(f"{self.nome} estuda por {self.carga_horaria} horas semanais")
        print("-" * 30)

    def mostrar_dados(self):
        print(f"Estagiário(a) {self.nome} possui um salário de: {self.salario} reais")
        print("-" * 30)



ger = Gerente("Claudin", 10000, 600)
ger.mostrar_dados()

dev = Desenvolvedor("Nicole", 50000, "Node.js")
dev.mostrar_dados()
dev.programar()  

est = Estagiario("Jurema", 2000, 7)
est.mostrar_dados()
est.estudar()