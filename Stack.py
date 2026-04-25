class Stack:
    """
    Stack (Pilha) — LIFO: Last In, First Out
    Implementada com array (lista Python).

    Complexidades:
        push()     → O(1)
        pop()      → O(1)
        peek()     → O(1)
        is_empty() → O(1)
        size()     → O(1)

    Onde aparece no mundo real:
        - Call Stack da JVM / Python runtime
        - Ctrl+Z (Undo) em qualquer editor
        - Botão "voltar" do browser
        - ROLLBACK de transações SQL
    """

    def __init__(self):
        self._dados = []

    def push(self, valor):
        self._dados.append(valor)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop em pilha vazia")
        return self._dados.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek em pilha vazia")
        return self._dados[-1]

    def is_empty(self):
        return len(self._dados) == 0

    def size(self):
        return len(self._dados)

    def __repr__(self):
        return f"Stack({self._dados})"


def validar_parenteses(expressao):
    """
    Usa a Stack para verificar se uma expressão tem parênteses balanceados.
    Caso de uso real: parsers de HTML, JSON, compiladores.

    Lógica:
        - Abre colchete/parêntese → empilha
        - Fecha → verifica se o topo é o par correspondente
        - No final, pilha deve estar vazia
    """
    pilha = Stack()
    pares = {')': '(', ']': '[', '}': '{'}
    abre = set('([{')

    for char in expressao:
        if char in abre:
            pilha.push(char)
        elif char in pares:
            if pilha.is_empty() or pilha.peek() != pares[char]:
                return False
            pilha.pop()

    return pilha.is_empty()


if __name__ == "__main__":
    casos = [
        ("((()))",   True),
        ("((())",    False),
        ("({[]})",   True),
        ("({[}])",   False),
        ("[]{}()",   True),
        ("",         True),
    ]

    print("=" * 45)
    print("   STACK — Balanced Parentheses Validator")
    print("=" * 45)
    todos_ok = True
    for expr, esperado in casos:
        resultado = validar_parenteses(expr)
        status = "✅ PASS" if resultado == esperado else "❌ FAIL"
        if resultado != esperado:
            todos_ok = False
        label = "válido" if resultado else "inválido"
        print(f"  {status}  {repr(expr):<12} → {label}")

    print("-" * 45)
    print(f"  {'Todos os testes passaram!' if todos_ok else 'Falhou!'}")
    print("=" * 45)