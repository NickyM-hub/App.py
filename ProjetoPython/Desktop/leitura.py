def ler_arquivo(caminho_arquivo):
    arquivo = None
    try:
        arquivo = open(caminho_arquivo, 'r')
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
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