import sys
from collections import deque


def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    dimensions = [int(n) for n in file.readline().split()]
    n_vert = dimensions[0]
    n_edj = dimensions[1]

    # adj_list = [[] for _ in range(n_vert)]
    adj_mat = [[0 for _ in range(n_vert)] for _ in range(n_vert)]

    # Read input line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        # adj_list[line_arr[0]].append(line_arr[1])
        # adj_list[line_arr[1]].append(line_arr[0])

        adj_mat[line_arr[0]][line_arr[1]] = 1
        adj_mat[line_arr[1]][line_arr[0]] = 1
    file.close()

    # for list in adj_list:
    #     print(list)
    # print()
    #
    # for list in adj_mat:
    #     print(list)
    # print()

    # Approach: traverse graph using bfs and color it

    bipartite = True

    # Initially all vertices are colored -1.
    colors = [-1 for _ in range(n_vert)]

    for i in range(n_vert):
        if colors[i] == -1:
            if not is_bipartite(adj_mat, i, colors):
                bipartite = False
                break

    if bipartite:
        print("YES")
    else:
        print("NO")


def is_bipartite(adj_mat, src_v, colors):
    colors[src_v] = 1

    queue = deque()
    queue.append(src_v)

    while queue:
        v = queue.popleft()

        # If self loop exists, graph is not bipartite
        if adj_mat[v][v] == 1:
            return False

        for adjV, edge in enumerate(adj_mat[v]):
            if edge == 1 and colors[adjV] == -1:
                colors[adjV] = 1 - colors[v]
                queue.append(adjV)

            elif edge == 1 and colors[adjV] == colors[v]:
                return False

    return True


if __name__ == "__main__":
    main()
