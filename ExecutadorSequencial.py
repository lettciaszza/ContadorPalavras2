import time
from ContadorSequencial import contar_palavras

def medir_tempo_execucao(nome_arquivo, num_execucoes):
    tempos = []
    for _ in range(num_execucoes):
        inicio = time.time()
        contar_palavras(nome_arquivo)
        fim = time.time()
        tempo_execucao = fim - inicio
        tempos.append(tempo_execucao)
    tempo_medio = sum(tempos) / num_execucoes
    return tempo_medio

if __name__ == "__main__":
    nome_arquivo = "./hamletSequencial.txt"

    # a) Apenas o tempo de uma execução do programa 1
    tempo_execucao_a = medir_tempo_execucao(nome_arquivo, 1)
    print(f"a) Tempo de uma execução: {tempo_execucao_a} segundos")

    # b) Tempo médio de 5 execuções do programa 1
    tempo_execucao_b = medir_tempo_execucao(nome_arquivo, 5)
    print(f"b) Tempo médio de 5 execuções: {tempo_execucao_b} segundos")

    # c) Tempo médio de 10 execuções do programa 1
    tempo_execucao_c = medir_tempo_execucao(nome_arquivo, 10)
    print(f"c) Tempo médio de 10 execuções: {tempo_execucao_c} segundos")

    # d) Tempo médio de 50 execuções do programa 1
    tempo_execucao_d = medir_tempo_execucao(nome_arquivo, 50)
    print(f"d) Tempo médio de 50 execuções: {tempo_execucao_d} segundos")

    # e) Tempo médio de 100 execuções do programa 1
    tempo_execucao_e = medir_tempo_execucao(nome_arquivo, 100)
    print(f"e) Tempo médio de 100 execuções: {tempo_execucao_e} segundos")
