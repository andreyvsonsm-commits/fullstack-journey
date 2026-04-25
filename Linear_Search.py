def busca_linear(arr, alvo):
    """
    Linear Search — O(n)
    Percorre o array elemento por elemento até encontrar o alvo.
    Complexidade: O(n) no pior caso, O(1) no melhor caso.
    """
    comparacoes = 0
    for i in range(len(arr)):
        comparacoes += 1
        if arr[i] == alvo:
            return i, comparacoes
    return -1, comparacoes


if __name__ == "__main__":
    array = [2, 5, 8, 12, 16, 23, 38, 45, 67, 91]
    alvo = 23

    idx, comps = busca_linear(array, alvo)

    print("=" * 45)
    print("        LINEAR SEARCH — O(n)")
    print("=" * 45)
    print(f"  Array : {array}")
    print(f"  Alvo  : {alvo}")
    print(f"  Índice: {idx}")
    print(f"  Comparações realizadas: {comps}")
    print()
    print("  Simulação com 1.000.000 de elementos:")
    print("  → Pior caso: até 1.000.000 comparações")
    print("=" * 45)