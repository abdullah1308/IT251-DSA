import sys


# Using BFS as the searching algorithm
def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = [s]

    visited[s] = True

    while queue:

        u = queue.pop(0)

        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


# Ford Fulkerson algorithm
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Adding the path flows
        max_flow += path_flow

        # Updating the residual values of edges
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


def main():
    if len(sys.argv) != 2:
        return

    file = open(sys.argv[1], 'r')

    n, m, s, t = [int(i) for i in file.readline().split()]

    adj_mat = [[0 for _ in range(n)] for _ in range(n)]

    for line in file:
        u, v, c = [int(i) for i in line.split()]
        adj_mat[u][v] = c

    # print("Adjacency matrix")
    # for vtx, row in enumerate(adj_mat):
    #     print(vtx, row)
    # print()

    print(ford_fulkerson(adj_mat, s, t))

if __name__ == '__main__':
    main()
