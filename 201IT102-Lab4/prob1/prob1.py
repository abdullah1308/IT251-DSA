import sys

discovery_time = 0


def find_bridges(adj_list):
    # Setting the discovery time, minimum time to reach an adjacent node, and parent of every node
    # to be -1.

    disc_times = [-1 for _ in range(len(adj_list))]
    parents = [-1 for _ in range(len(adj_list))]
    min_adj_time = [-1 for _ in range(len(adj_list))]

    bridges = []

    dfs(0, adj_list, disc_times, min_adj_time, parents, bridges)

    if bridges:
        print("NO")
        for bridge in bridges:
            print(bridge[0], bridge[1])
    else:
        print("YES")


def dfs(source, adj_list, disc_times, min_adj_time, parents, bridges):
    # time is set as global, so that it retains changes to its value during recursion
    global discovery_time

    disc_times[source] = discovery_time
    min_adj_time[source] = discovery_time

    discovery_time += 1

    for adj_vertex in adj_list[source]:

        if disc_times[adj_vertex] == -1:  # If adj_vertex is never visited
            parents[adj_vertex] = source
            dfs(adj_vertex, adj_list, disc_times, min_adj_time, parents, bridges)
            min_adj_time[source] = min(min_adj_time[adj_vertex], min_adj_time[source])

            if min_adj_time[adj_vertex] > disc_times[source]:
                bridges.append([source, adj_vertex])

        elif adj_vertex != parents[source]:  # Ignoring child to parent edge
            min_adj_time[source] = min(min_adj_time[source], disc_times[adj_vertex])


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
    # adj_mat = [[0 for _ in range(n_vert)] for _ in range(n_vert)]

    # Read input line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        adj_list[line_arr[0]].append(line_arr[1])
        adj_list[line_arr[1]].append(line_arr[0])

        # adj_mat[line_arr[0]][line_arr[1]] = 1
        # adj_mat[line_arr[1]][line_arr[0]] = 1
    file.close()

    # for vertex, list in enumerate(adj_list):
    #     print(vertex, list)
    # print()

    # for list in adj_mat:
    #     print(list)
    # print()

    # Approach - Traverse through the graph using dfs to find bridges using
    # Tarjan's algorithm. If no bridges exist then the graph is 2-edge connected.

    find_bridges(adj_list)


if __name__ == "__main__":
    main()
