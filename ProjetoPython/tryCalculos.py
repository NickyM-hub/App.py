def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def divisao(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        return None

def multiplicacao(a, b):
    return a * b

def calcular():
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    
    operacao = input('Escolha uma operação (soma, subtracao, divisao, multiplicacao): ')
    
    if operacao == "soma":
        resultado = soma(a, b)
    elif operacao == "subtracao":
        resultado = subtracao(a, b)
    elif operacao == "divisao":
        resultado = divisao(a, b)
    elif operacao == "multiplicacao":
        resultado = multiplicacao(a, b)
    else:
        print("Operação inválida.")
        return

    if resultado is not None:
        print(f'O resultado é: {resultado}')
    else:
        print('Operação não pôde ser realizada.')

calcular()