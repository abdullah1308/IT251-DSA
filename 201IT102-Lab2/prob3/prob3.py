import sys


def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    dimensions = [int(n) for n in file.readline().split()]
    n_vertex = dimensions[0]
    n_edge = dimensions[1]

    in_adj_list = [[] for i in range(n_vertex)]

    # Read input line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        in_adj_list[line_arr[0]].append(line_arr[1])

        if line_arr[0] != line_arr[1]:
            in_adj_list[line_arr[1]].append(line_arr[0])

    file.close()

    # print("Input Adjacency list representation: ")
    # for i in range(n_vertex):
    #     print(i, end=': ')
    #     for j in range(len(in_adj_list[i])):
    #         print(in_adj_list[i][j], end=' ')
    #     print()

    # Approach: Add all the adjacent vertices for a vertex 
    # except the vertex itself into a set.
    
    res_adj_list = []

    for idx, adj_vertices in enumerate(in_adj_list):
        vertex_set = set()

        for adj_vertex in adj_vertices:
            if idx != adj_vertex:
                vertex_set.add(adj_vertex)

        res_adj_list.append([vertex for vertex in vertex_set])

    print("Adjacency list representation of G': ")
    for i in range(n_vertex):
        print(i, end=': ')
        for j in range(len(res_adj_list[i])):
            print(res_adj_list[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
