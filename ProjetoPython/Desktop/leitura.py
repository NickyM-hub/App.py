def ler_arquivo(caminho_arquivo):
    arquivo = None
    try:
        arquivo = open('/home/nicole/Área de trabalho/HelloWorld.txt', 'r')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{'/home/nicole/Área de trabalho/HelloWorld.txt'}' não foi encontrado.")
    else:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
    finally:
        if arquivo is not None:
            try:
                arquivo.close()
                print("Arquivo fechado com sucesso.")
            except Exception as e:
                print(f"Erro ao fechar o arquivo: {e}")