import math
import sys


def main():
    if len(sys.argv) != 2:
        return

    file = open(sys.argv[1], 'r')

    n, m, s = [int(i) for i in file.readline().split()]

    adj_mat = [[0 for _ in range(n)] for _ in range(n)]
    edj_list = []

    for line in file:
        v1, v2, wt = [int(i) for i in line.split()]
        adj_mat[v1][v2] = wt
        edj_list.append([v1, v2])

    # print("Adjacency matrix")
    # for vtx, row in enumerate(adj_mat):
    #     print(vtx, row)

    cost = [math.inf for _ in range(n)]
    cost[s] = 0
    paths = [[] for _ in range(n)]
    paths[s].append(s)

    isRelaxed = False

    for _ in range(n):
        isRelaxed = False
        for edj in edj_list:
            v1 = edj[0]
            v2 = edj[1]

            if cost[v1] + adj_mat[v1][v2] < cost[v2]:
                cost[v2] = cost[v1] + adj_mat[v1][v2]
                paths[v2] = paths[v1][:]
                paths[v2].append(v2)
                isRelaxed = True

        if not isRelaxed:
            break

    if isRelaxed:
        print("Graph has a negative weight cycle.")
    else:
        for vtx, path in enumerate(paths):
            print("Shortest path to", vtx, ":", path, "| cost =", cost[vtx])


if __name__ == '__main__':
    main()
