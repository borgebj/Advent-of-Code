import random
from algoritmer.python_algoritmer.grafer.AdjacencyList import AdjacencyList


def fillRandom(graph):
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    weights = [1, 2, 3, 4, 5]
    for y in range(len(nodes)): graph.addNode(nodes[y])  # sørger for alfabetisk rekkefølge
    for x in range(10):
        one = random.choice(nodes)
        two = random.choice(nodes)
        weight = random.choice(weights)
        if one != two:
            if graph.weights: graph.addEdge(one, two, weight)
            else: graph.addEdge(one, two)


# Hoved-funksjonen for denne filen #
def BFS(graph, startnode):
    visited = [startnode]
    queue = [startnode]
    path = []

    while queue:
        node = queue.pop(0)
        path.append(node)
        for nabo in graph[node]:
            if nabo not in visited:
                visited.append(nabo)
                queue.append(nabo)
    return path


def main():
    graph = AdjacencyList(weights=True)
    print("< Opprettet med graf med maks 10 kanter >")
    fillRandom(graph)
    graph.drawgraph()
    print("---------------")
    graph.printGraph()
    print("BFS traversering")
    print(graph.BFS(input("Startsnode: ")))
    print("--------------------------------------------")
    print("BFS traversering for korteste vei")
    print(graph.BFS_shortest_path(input("Start: "), input("Slutt: ")))


main()
