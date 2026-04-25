def anagrama_on2(s1, s2):
    """
    Verificação de anagrama — O(n²)
    Para cada caractere de s1, busca em s2 e remove se encontrar.
    Ineficiente: loop dentro de loop.
    """
    if len(s1) != len(s2):
        return False

    lista = list(s2)
    for char in s1:
        if char in lista:          # O(n) dentro de um loop O(n) = O(n²)
            lista.remove(char)
        else:
            return False
    return True


def anagrama_on(s1, s2):
    """
    Verificação de anagrama — O(n)
    Usa uma Hash Table para contar frequência de cada letra.
    Motivo da eficiência: acesso à hash table é O(1) por chave.

    Conexão com BD: é exatamente como um índice HASH funciona no PostgreSQL.
    """
    if len(s1) != len(s2):
        return False

    contagem = {}  # Hash Table

    for char in s1:
        contagem[char] = contagem.get(char, 0) + 1

    for char in s2:
        if char not in contagem or contagem[char] == 0:
            return False
        contagem[char] -= 1

    return True


if __name__ == "__main__":
    pares = [
        ("listen", "silent"),
        ("hello",  "world"),
        ("anagram","nagaram"),
        ("rat",    "car"),
    ]

    print("=" * 55)
    print("         ANAGRAM CHECKER — O(n²) vs O(n)")
    print("=" * 55)
    print(f"  {'Par':<25} {'O(n²)':^8} {'O(n)':^8}")
    print("-" * 55)
    for s1, s2 in pares:
        r1 = anagrama_on2(s1, s2)
        r2 = anagrama_on(s1, s2)
        icone1 = "✅" if r1 else "❌"
        icone2 = "✅" if r2 else "❌"
        print(f"  {s1!r:>10} / {s2!r:<12}  {icone1:^8} {icone2:^8}")
    print("=" * 55)
    print()
    print("  Por que O(n) é melhor?")
    print("  → Hash Table: acesso a contagem[char] = O(1)")
    print("  → Equivale ao HASH INDEX do PostgreSQL")
    print("=" * 55)