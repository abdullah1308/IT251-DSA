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


# Searches given word in a given matrix
def patternSearch(grid, dictionary):
    R = len(grid)
    C = len(grid[0])

    res = set()

    for word in dictionary:
        for row in range(R):
            for col in range(C):
                if search2D(grid, row, col, word):
                    res.add(word)

    return res


# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
dir = [[-1, -1], [-1, 1], [-1, 0], [0, -1], [1, -1], [0, 1], [1, 0], [1, 1]]


# This function searches in all 8-direction from point(row, col) in grid[][]
def search2D(grid, row, col, word):
    R = len(grid)
    C = len(grid[0])

    if grid[row][col] != word[0]:
        return False

    for x, y in dir:

        rd, cd = row + x, col + y
        flag = True

        for k in range(1, len(word)):

            # If out of bound or not matched, break
            if (0 <= rd < R and
                    0 <= cd < C and
                    word[k] == grid[rd][cd]):

                # Moving in particular direction
                rd += x
                cd += y
            else:
                flag = False
                break

        # If all character matched, then
        # value of flag must be false
        if flag:
            return True
    return False


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

    # insert all words into a trie
    trie = Trie()
    for word in dictionary:
        insert(trie, word)

    # for word in dictionary:
    #     print(word)

    res = patternSearch(matrix, dictionary)
    result = []

    for word in res:
        result.append(word)

    result.sort()

    for word in result:
        print(word)


if __name__ == '__main__':
    main()
