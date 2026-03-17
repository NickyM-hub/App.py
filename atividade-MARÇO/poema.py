def ler_arquivo():
  try:
      with open("poema.txt", "r") as arquivo:
          conteudo = arquivo.read()
          print("Conteúdo Atual:")
          print(conteudo)
  except FileNotFoundError:
      print("O arquivo ainda não foi criado.")


ler_arquivo()