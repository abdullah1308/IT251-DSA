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
    src = dimensions[2]
    dest = dimensions[3]

    if src == dest:
        print(1)
        sys.exit()

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

    for vertex, list in enumerate(adj_list):
        print(vertex, list)
    print()

    # for list in adj_mat:
    #     print(list)
    # print()

    # Approach : Traverse graph using bfs and sum the number of paths from u to v.
    result = 0
    queue = deque()
    visited = [False for _ in range(n_vert)]
    count = [0 for _ in range(n_vert)]

    queue.append(src)
    count[src] = 1
    visited[src] = True

    while True:
        





    while queue:
        v = queue.popleft()
        visited[v] = True

        for adjV in adj_list[v]:
            if adjV == dest:
                result = result + 1
            elif adjV != parent[v]:
                parent[adjV] = v
                queue.append(v)

    print(result)

if __name__ == "__main__":
    main()