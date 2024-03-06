from collections import deque

def eh_objetivo(estado, objetivo):
    return estado == objetivo

def gerar_vizinhos(estado):
    vizinhos = []
    posicao_zero = None

    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                posicao_zero = (i, j)       
                break

    for movimento in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nova_posicao = (posicao_zero[0] + movimento[0], posicao_zero[1] + movimento[1])
        if 0 <= nova_posicao[0] < 3 and 0 <= nova_posicao[1] < 3:
            novo_estado = [linha.copy() for linha in estado]
            novo_estado[posicao_zero[0]][posicao_zero[1]] = estado[nova_posicao[0]][nova_posicao[1]]
            novo_estado[nova_posicao[0]][nova_posicao[1]] = 0
            vizinhos.append(novo_estado)

    return vizinhos

def bfs(inicial, objetivo):
    fila = deque([(inicial, 0)])
    visitados = set()

    while fila:
        estado_atual, num_movimentos = fila.popleft()

        if tuple(map(tuple, estado_atual)) in visitados:
            continue

        visitados.add(tuple(map(tuple, estado_atual)))

        if eh_objetivo(estado_atual, objetivo):
            return num_movimentos, estado_atual

        vizinhos = gerar_vizinhos(estado_atual)

        for estado_vizinho in vizinhos:
            fila.append((estado_vizinho, num_movimentos + 1))

    return None

# Exemplo de uso:
estado_inicial = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

estado_objetivo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

resultado = bfs([linha.copy() for linha in estado_inicial], estado_objetivo)

if resultado is not None:
    num_movimentos, matriz_final = resultado
    print(f"Número de movimentos necessários: {num_movimentos}")
    print("Matriz Final:")
    for linha in matriz_final:
        print(linha)
else:
    print("Não foi possível encontrar uma solução.")