# Кол-во вершин
n = 5

# Список дуг
edges = [
    (0, 1),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 1),
    (4, 0),
    (4, 2),
    (4, 3)
]

# Матрица смежности
def to_adjacency_matrix(edges, n):
    A = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in edges:
        A[i][j] = 1
    return A


# Матрица инцидентности
def to_incidence_matrix(edges, n):
    B = [[0 for _ in range(len(edges))] for _ in range(n)]
    for k, (i, j) in enumerate(edges):
        B[i][k] = 1
        B[j][k] = -1
    return B


# Список смежности
def to_adjacency_list(edges, n):
    C = {i: [] for i in range(n)}
    for i, j in edges:
        C[i].append(j)
    return C


# Список дуг
def to_edge_list(edges):
    return edges.copy()

A = to_adjacency_matrix(edges, n)
B = to_incidence_matrix(edges, n)
C = to_adjacency_list(edges, n)
E = to_edge_list(edges)

if __name__ == "__main__":
    # Выводим представления
    print("Матрица смежности:")
    for row in A:
        print(row)

    print("\nМатрица инцидентности:")
    for row in B:
        print(row)

    print("\nСписок смежности:")
    print(C)

    print("\nСписок дуг:")
    print(E)