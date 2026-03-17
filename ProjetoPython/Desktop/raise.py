idade = 25
def verificar_idade(idade):
    if idade < 0 or idade > 150:
        raise ValueError("A idade é inválida! Deve estar entre 0 e 150.")
    else:
        print("Idade aceita com sucesso.")

def teste_funcao():
    teste = [25, -5, 160]

    for valor in teste:
        try:
            print(f"Testando idade: {valor}")
            verificar_idade(valor)
        except ValueError as i:
            print(f"Erro capturado: {i}")

teste_funcao()