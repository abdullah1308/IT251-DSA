import sys

discovery_time = 0


def find_articulation_pts(adj_list):
    n_vert = len(adj_list)

    discovery = [-1 for _ in range(n_vert)]
    parents = discovery[:]
    min_adj_time = discovery[:]
    articulation_pts = [False for _ in range(n_vert)]

    # for vertex in range(n_vert):
    #     if discovery[vertex] == -1:
    dfs(0, adj_list, discovery, min_adj_time, parents, articulation_pts)

    if True in articulation_pts:
        print("Articulation points found:")
        for vertex, value in enumerate(articulation_pts):
            if value:
                print(vertex)
    else:
        print("Biconnected Graph")


def dfs(source, adj_list, discovery, min_adj_time, parents, articulation_pts):
    # time is set as global, so that it retains changes to its value during recursion
    global discovery_time

    discovery[source] = discovery_time
    min_adj_time[source] = discovery_time
    discovery_time += 1
    n_children = 0

    for adj_vert in adj_list[source]:
        if discovery[adj_vert] == -1:  # If adjacent vertex is not visited
            n_children += 1
            parents[adj_vert] = source
            dfs(adj_vert, adj_list, discovery, min_adj_time, parents, articulation_pts)
            min_adj_time[source] = min(min_adj_time[source], min_adj_time[adj_vert])

            if parents[source] == -1 and n_children > 1:  # Checking if root is an articulation point
                articulation_pts[source] = True

            if parents[source] != -1 and min_adj_time[adj_vert] >= discovery[source]:
                articulation_pts[source] = True

        elif adj_vert != parents[source]:
            min_adj_time[source] = min(min_adj_time[source], discovery[adj_vert])


def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    dimensions = [int(n) for n in file.readline().split()]
    n_vert = dimensions[0]
    n_edj = dimensions[1]

    adj_list = [[] for _ in range(n_vert)]
    adj_mat = [[0 for _ in range(n_vert)] for _ in range(n_vert)]

    # Read input file line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        adj_list[line_arr[0]].append(line_arr[1])
        adj_list[line_arr[1]].append(line_arr[0])

        # adj_mat[line_arr[0]][line_arr[1]] = 1
        # adj_mat[line_arr[1]][line_arr[0]] = 1

    # for vertex, list in enumerate(adj_list):
    #     print(vertex, list)
    # print()

    # for list in adj_mat:
    #     print(list)
    # print()

    # Approach - Traverse through the graph using dfs and find articulation
    # points using Tarjan's algorithm.

    find_articulation_pts(adj_list)


if __name__ == "__main__":
    main()
