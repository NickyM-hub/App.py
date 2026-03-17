def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    divisao = a / b
    multiplicacao = a * b
    return soma, subtracao, divisao, multiplicacao

def calcular():
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    
    operacao = input('Escolha uma operação (soma, subtracao, divisao, multiplicacao): ')
    
    resultado_soma, resultado_subtracao, resultado_divisao, resultado_multiplicacao = operacoes(a, b)
    
    if operacao == "soma":
        resultado = resultado_soma
    elif operacao == "subtracao":
        resultado = resultado_subtracao
    elif operacao == "divisao":
        resultado = resultado_divisao
    elif operacao == "multiplicacao":
        resultado = resultado_multiplicacao
    else:
        return "Operação inválida"

    print(f"O resultado da {operacao} é: {resultado}")

calcular()