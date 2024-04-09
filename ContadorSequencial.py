def contar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            num_palavras = len(palavras)
            return num_palavras
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return 0
    

if __name__ == "__main__":
    nome_arquivo = "./hamletSequencial.txt"
    total_palavras = contar_palavras(nome_arquivo)
    print(f"O livro Hamlet do autor  William Shakespeare, contém: {total_palavras} palavras.")
