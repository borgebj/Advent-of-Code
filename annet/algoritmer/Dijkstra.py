import random
import graphviz
from algoritmer.python_algoritmer.grafer.AdjacencyList import AdjacencyList
from collections import defaultdict
from heapq import heappush,  _heappop_max,  _heapify_max


def fillRandom(graph):
    nodes = ["A", "B", "C", "D", "E", "F", "G"]
    weights = [1, 2, 3, 4, 5]
    for y in range(len(nodes)): graph.addNode(nodes[y])  # sørger for alfabetisk rekkefølge
    for x in range(10):
        one = random.choice(nodes)
        two = random.choice(nodes)
        weight = random.choice(weights)
        if one != two:
            if graph.weights:
                graph.addEdge(one, two, weight)
            else:
                graph.addEdge(one, two)


def drawDjikstra(graph, parents):
    dot = graphviz.Graph()
    for node in parents:
        u = parents[node]
        if u:
            dot.edge(node, u, label=str(graph[node][u]))
    dot.render("Dijkstra", format='svg')


# lambda: float vil si at dicten har default-verdi float
# for å finne korteste vei
def Dijkstra(graph, s):
    queue = [(0, s)]
    dist = defaultdict(lambda: float('inf'))
    parents = {s: None}
    dist[s] = 0

    while queue:
        cost, node = queue.pop(0)

        for nabo in graph[node]:
            c = cost + graph[nabo][node]
            if c < dist[nabo]:
                dist[nabo] = c
                queue.append((c, nabo))
                parents[nabo] = node

    return parents, dist


# for å finne lengste vei
def DijkstraHeaviest(graph, s):
    visited = [s]
    queue = [(0, s)]
    dist = defaultdict(lambda: 0)
    parents = {s: None}

    while queue:
        _heapify_max(queue)
        cost, highest = _heappop_max(queue)

        for nabo in graph[highest]:
            c = (10-(cost + graph[nabo][highest]))
            if c > dist[nabo] and nabo not in visited:
                visited.append(nabo)
                dist[nabo] = c
                heappush(queue, (c, nabo))
                parents[nabo] = highest

    return parents, dist


def printPath(parent, distances, dest, graph):
    global vekt
    if distances[dest] == 0:
        print("-------------------------")
        print("Start:", dest)
        return

    printPath(parent, distances, parent[dest], graph)
    vekt = distances[dest]
    print("===[", graph[dest][parent[dest]], "] ===>", dest)


vekt = 0


def main():
    graph = AdjacencyList(weights=True)

    # graf-del
    print("< Opprettet med graf med maks 10 kanter >")
    fillRandom(graph)
    print("---------------")

    # dijkstra-del
    print("Dijkstra traversering for korteste vei")
    valg = input("minst | størst: ")
    start = input("Start: ")
    slutt = input("Slutt: ")

    if valg.lower() == "minst":
        parents, distances = Dijkstra(graph.graph, start)
    else:
        parents, distances = DijkstraHeaviest(graph.graph, start)

    drawDjikstra(graph.graph, parents)
    printPath(parents, distances, slutt, graph.graph)
    print("Total vekt:", vekt)
    print("-------------------------")

main()
