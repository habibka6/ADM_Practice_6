from task2 import *

def graph_to_edges(graph, representation):
    result = []
    if representation == "матрица смежности":
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 1:
                    result.append((i, j))

    elif representation == "матрица инцидентности":
        for k in range(len(graph[0])):
            start = None
            end = None
            for i in range(len(graph)):
                if graph[i][k] == 1:
                    start = i

                if graph[i][k] == -1:
                    end = i

            result.append((start, end))

    elif representation == "список смежности":
        for i in graph:
            for j in graph[i]:
                result.append((i, j))

    elif representation == "список дуг":
        result = graph.copy()
    return result


def convert_graph(graph, from_representation, to_representation):
    edges = graph_to_edges(graph, from_representation)

    if to_representation == "матрица смежности":
        return to_adjacency_matrix(edges, n)

    elif to_representation == "матрица инцидентности":
        return to_incidence_matrix(edges, n)

    elif to_representation == "список смежности":
        return to_adjacency_list(edges, n)

    elif to_representation == "список дуг":
        return to_edge_list(edges)


print("Список дуг -> матрица смежности:")
new_A = convert_graph(E, "список дуг", "матрица смежности")

for row in new_A:
    print(row)

print()

print("Матрица смежности -> список смежности:")
new_C = convert_graph(A, "матрица смежности", "список смежности")
print(new_C)

print()

print("Список смежности -> матрица инцидентности:")
new_B = convert_graph(C, "список смежности", "матрица инцидентности")

for row in new_B:
    print(row)