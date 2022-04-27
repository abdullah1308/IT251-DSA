import sys


class Trie:
    def __init__(self):
        self.character = {}
        self.isLeaf = False  # true when the node is a leaf node


def insert(root, s):
    # start from the root node
    curr = root

    for ch in s:
        # go to the next node (create if the path doesn't exist)
        curr = curr.character.setdefault(ch, Trie())

    curr.isLeaf = True


# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
rowDir = [-1, -1, -1, 0, 1, 0, 1, 1]
colDir = [-1, 1, 0, -1, -1, 1, 0, 1]


# This function searches in all 8-direction from point(row, col) in grid[][]
def search2D(trie, grid, row, col, set):
    R = len(grid)
    C = len(grid[0])

    if grid[row][col] not in trie.character:
        return set

    # Search word in all 8 directions
    # starting from (row, col)
    for idx in range(len(rowDir)):

        x = rowDir[idx]
        y = colDir[idx]

        ch = grid[row][col]
        current = trie

        # Initialize  point
        # for current direction
        rd, cd = row + x, col + y
        flag = True

        while not current.isLeaf:
            if 0 <= rd < R and 0 <= cd < C and grid[rd][cd] in current.character:
                current = current.character[grid[rd][cd]]
                ch += grid[rd][cd]
                rd += x
                cd += y

            else:
                flag = False
                break

        print(set)

        if current.isLeaf and flag:
            set.add(ch)

    return set


# Searches given word in a given matrix
# in all 8 directions
def patternSearch(dictionary, grid):
    # Rows and columns in given grid
    R = len(grid)
    C = len(grid[0])

    # insert all words into a trie
    trie = Trie()
    for word in dictionary:
        insert(trie, word)

    result = set()

    # Consider every point as starting point
    # and search given word
    for row in range(R):
        for col in range(C):
            result.union(search2D(trie, grid, row, col, result))

    return result


def main():
    if len(sys.argv) != 2:
        return

    ip_file = open(sys.argv[1], 'r')
    matrix = []

    for line in ip_file:
        row = line.strip().split(' ')
        matrix.append(row)

    # for row in matrix:
    #     print(row)

    dict_file = open('small.dict', 'r')
    dictionary = []
    for line in dict_file:
        dictionary.append(line.strip())

    # for word in dictionary:
    #     print(word)

    resultSet = patternSearch(dictionary, matrix)
    result = []

    for word in resultSet:
        result.append(word)

    result.sort()

    # print("Here")

    for word in result:
        print(word)




if __name__ == '__main__':
    main()
