import sys

def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    adj_mat = []

    # Read input line by line
    for line in file:
        row = [int(n) for n in line.split()]
        # print(row)
        adj_mat.append(row)

    file.close()

    # Approach: vertices having a row containing all zeroes are candidate sinks
    candidates = []

    # print()
    # print(adj_mat)
    # print()

    for idx, row in enumerate(adj_mat):
        contains1 = False

        for elem in row:
            if elem == 1:
                contains1 = True
                break

        if not contains1:
            candidates.append(idx)

    # print(candidates)
    # print()

    # Verifying candidates
    for cad in candidates:
        contains0 = False

        for row in range(len(adj_mat)):
            if row == cad:
                continue
            # print(row, cad, adj_mat[row][cad])
            if adj_mat[row][cad] == 0:
                contains0 = True
                break

        if not contains0:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
