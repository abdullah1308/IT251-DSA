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

    adj_list = [[] for i in range(n_vertex)]
    adj_mat = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]

    # Read input line by line
    for line in file:
        line_arr = [int(n) for n in line.split()]

        adj_list[line_arr[0]].append(line_arr[1])
        adj_list[line_arr[1]].append(line_arr[0])

        adj_mat[line_arr[0]][line_arr[1]] = 1
        adj_mat[line_arr[1]][line_arr[0]] = 1
    file.close()

    print("Adjacency list representation: ")
    for i in range(n_vertex):
        print(i, end=': ')
        for j in range(len(adj_list[i])):
            print(adj_list[i][j], end=' ')
        print()

    print("Adjacency matrix representation: ")
    for i in range(n_vertex):
        for j in range(n_vertex):
            print(adj_mat[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()
