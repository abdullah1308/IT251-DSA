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
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


# The function returns false if (x, y) is not valid matrix coordinates
# or cell (x, y) is already processed or doesn't lead to the solution
def isSafe(x, y, processed, board, ch):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0])) and \
           not processed[x][y] and (board[x][y] == ch)


# A recursive function to search valid words present in a matrix using trie
def searchMatrix(root, board, i, j, processed, path, result):
    # if a leaf node is encountered
    if root.isLeaf:
        # update result with the current word
        result.add(path)

    # mark the current cell as processed
    processed[i][j] = True

    # traverse all children of the current Trie node
    for key, value in root.character.items():

        # check for all eight possible movements from the current cell
        for k in range(len(row)):

            # skip if a cell is invalid, or it is already processed
            # or doesn't lead to any path in the Trie
            if isSafe(i + row[k], j + col[k], processed, board, key):
                searchMatrix(value, board, i + row[k], j + col[k],
                             processed, path + key, result)

    # backtrack: mark the current cell as unprocessed
    processed[i][j] = False


# Function to search for a given set of words in a matrix
def searchInMatrix(board, words):
    # construct a set for storing the result
    result = set()

    # base case
    if not board or not len(board):
        return

    # insert all words into a trie
    root = Trie()
    for word in words:
        insert(root, word)

    # `M × N` board
    (M, N) = (len(board), len(board[0]))

    # construct a matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]

    # consider each character in the matrix
    for i in range(M):
        for j in range(N):
            ch = board[i][j]  # current character

            # proceed only if the current character is a child of the Trie root node
            if ch in root.character:
                searchMatrix(root.character[ch], board, i, j, processed, ch, result)

    # return the result set
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

    validWords = searchInMatrix(matrix, dictionary)
    res = []
    for word in validWords:
        res.append(word)

    res.sort()

    for word in res:
        print(word)


if __name__ == '__main__':
    main()
