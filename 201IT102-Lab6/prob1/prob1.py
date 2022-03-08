import math
import sys


def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    dimensions = [int(n) for n in file.readline().split()]
    n_vert = dimensions[0]
    n_edj = dimensions[1]
    src = dimensions[2]

    # adj_list = [[] for _ in range(n_vert)]
    adj_mat = [[0 for _ in range(n_vert)] for _ in range(n_vert)]

    # Read input line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        adj_mat[line_arr[0]][line_arr[1]] = line_arr[2]
        adj_mat[line_arr[1]][line_arr[0]] = line_arr[2]
    file.close()

    # for vertex, list in enumerate(adj_list):
    #     print(vertex, list)
    # print()

    # for list in adj_mat:
    #     print(list)
    # print()

    parents = [[0] for _ in range(n_vert)]
    cost = [math.inf for _ in range(n_vert)]
    cost[src] = 0
    processed = [False for _ in range(n_vert)]

    for i in range(n_vert - 1):
        vertex = minVertex(cost, processed)
        processed[vertex] = True

        for adjV, edj in enumerate(adj_mat[vertex]):
            if (edj != 0 and not processed[adjV] and cost[vertex] + edj < cost[adjV]):
                cost[adjV] = cost[vertex] + edj
                parents[adjV] = [i for i in parents[vertex]]
                parents[adjV].append(adjV)

    for vtx, cst in enumerate(cost):
        print("Shortest path to", vtx, ":", parents[vtx], "cost =", cst)


def minVertex(cost, processed):
    vertex = None
    minimum = math.inf
    for vtx, cst in enumerate(cost):
        if (not processed[vtx] and cst < minimum):
            vertex = vtx
            minimum = cst

    return vertex


if __name__ == "__main__":
    main()
