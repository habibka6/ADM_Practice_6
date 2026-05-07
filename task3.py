from task2 import *

def outgoing_edges(graph, representation, vertex):
    result = []

    # Матрица смежности
    if representation == "матрица смежности":
        for j in range(len(graph[vertex])):
            if graph[vertex][j] == 1:
                result.append((vertex, j))

    # Матрица инцидентности
    elif representation == "матрица инцидентности":
        for k in range(len(graph[0])):
            if graph[vertex][k] == 1:
                for i in range(len(graph)):
                    if graph[i][k] == -1:
                        result.append((vertex, i))

    # Список смежности
    elif representation == "список смежности":
        for j in graph[vertex]:
            result.append((vertex, j))

    # Список дуг
    elif representation == "список дуг":
        for i, j in graph:
            if i == vertex:
                result.append((i, j))
    return result


for i in range(5):
    print("Матрица смежности:")
    print(outgoing_edges(A, "матрица смежности", i))
    print()

    print("Матрица инцидентности:")
    print(outgoing_edges(B, "матрица инцидентности", i))
    print()

    print("Список смежности:")
    print(outgoing_edges(C, "список смежности", i))
    print()

    print("Список дуг:")
    print(outgoing_edges(E, "список дуг",i))