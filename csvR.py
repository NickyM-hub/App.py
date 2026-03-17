import csv

def ler_arquivo():
    with open('alunos.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

def adicionar_conteudo():
    with open('alunos.csv', 'a') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(["Maria", 22, "Medicina"])
        
adicionar_conteudo()
ler_arquivo()