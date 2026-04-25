def busca_linear(arr, alvo):
    comparacoes = 0
    for i in range(len(arr)):
        comparacoes += 1
        if arr[i] == alvo:
            return i, comparacoes
    return -1, comparacoes


def busca_binaria(arr, alvo):
    inicio = 0
    fim = len(arr) - 1
    comparacoes = 0

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2

        if arr[meio] == alvo:
            return meio, comparacoes
        elif arr[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes