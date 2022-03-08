import sys
from collections import deque
from sys import maxsize as INT_MAX

# Ensure number of arguments is two    
if len(sys.argv) == 2:
    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')
    # Read input line by line
    i = 0
    for line in file:
        if i == 0:
            n, m, src, end = line.strip().split(" ")
            n, m, src, end = int(n), int(m), int(src), int(end)
            adjList = [[] for i in range(n)]
            visited = [-1 for i in range(n)]
        else:
            p1, p2 = line.strip().split(" ")
            p1, p2 = int(p1), int(p2)
            if p2 not in adjList[p1]:
                adjList[p1].append(p2)
            if p1 not in adjList[p2]:
                adjList[p2].append(p1)
        i += 1

    # print(list(enumerate(adjList)))


def BFS(adj, src, dist, paths, n):
    visited = [False] * n
    dist[src] = 0
    paths[src] = 1

    q = deque()
    q.append(src)
    visited[src] = True
    while q:
        curr = q[0]
        q.popleft()

        for x in adj[curr]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
            if dist[x] > dist[curr] + 1:
                dist[x] = dist[curr] + 1
                paths[x] = paths[curr]
            elif dist[x] == dist[curr] + 1:
                paths[x] += paths[curr]


dist = [INT_MAX for i in range(n)]
paths = [0 for i in range(n)]
BFS(adjList, src, dist, paths, n)
# print("Numbers of shortest Paths are:", end=" ")
# for i in paths:
# 	print(i, end=" ")
print(f"{paths[end]}")
