def busca_binaria(arr, alvo)
    
    Binary Search — O(log n)
    Divide o array ao meio a cada iteração, descartando metade dos elementos.
    Complexidade O(log n) no pior caso, O(1) no melhor caso.
    REQUISITO o array deve estar ordenado.
    
    inicio = 0
    fim = len(arr) - 1
    comparacoes = 0

    while inicio = fim
        comparacoes += 1
        meio = (inicio + fim)  2

        if arr[meio] == alvo
            return meio, comparacoes
        elif arr[meio]  alvo
            inicio = meio + 1
        else
            fim = meio - 1

    return -1, comparacoes


if __name__ == __main__
    array = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91]
    alvo = 23

    idx, comps = busca_binaria(array, alvo)

    print(=  45)
    print(       BINARY SEARCH — O(log n))
    print(=  45)
    print(f  Array  {array})
    print(f  Alvo   {alvo})
    print(f  Índice {idx})
    print(f  Comparações realizadas {comps})
    print()
    print(  Simulação com 1.000.000 de elementos)
    print(  → Pior caso até ~20 comparações)
    print(  → Isso é um índice B-Tree na prática!)
    print(=  45)