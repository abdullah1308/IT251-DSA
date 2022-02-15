import sys
from collections import deque


# Takes in a number and returns its row and column in the board
def square_to_rc(square):
    # 1 is subtracted as matrix is zero indexed
    r = (square - 1) // 10
    c = (square - 1) % 10

    # Odd rows have reverse ordering
    if r % 2:
        c = 10 - 1 - c
    return [r, c]


def min_moves(board):
    # Approach: Traverse the board using bfs

    q = deque()

    # Queue contains an array of square number, number of moves taken to reach the square
    # and squares in the path.
    q.append([1, 0, []])

    # Hashset to store previously visited squares
    visit = set()

    while q:
        square, moves, path = q.popleft()
        # print(square, moves, path)

        for i in range(1, 7):
            nextSquare = square + i
            r, c = square_to_rc(nextSquare)

            if board[r][c] != -1:
                nextSquare = board[r][c]

            if nextSquare == 100:
                res_path = path[:]
                res_path.append(square)
                if square + i != 100:
                    res_path.append(square + i)
                res_path.append(100)
                return moves + 1, res_path

            if nextSquare not in visit:
                visit.add(nextSquare)
                continue_path = path[:]
                continue_path.append(square)
                if square + i != nextSquare:
                    continue_path.append(square + i)
                q.append([nextSquare, moves + 1, continue_path])

    return -1


def main():
    # Ensure number of arguments is two
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1]  # Second argument is the file name.
    file = open(fname, 'r')

    n_snake, n_ladder = [int(n) for n in file.readline().split()]

    snakes = []
    for _ in range(n_snake):
        snake = [int(n) for n in file.readline().split()]
        snakes.append(snake)

    ladders = []
    for _ in range(n_ladder):
        ladder = [int(n) for n in file.readline().split()]
        ladders.append(ladder)

    # Initializing a 10 x 10 board
    board = [[-1 for _ in range(10)] for _ in range(10)]

    for start, end in snakes:
        rS, cS = square_to_rc(start)

        board[rS][cS] = end

    for start, end in ladders:
        rS, cS = square_to_rc(start)

        board[rS][cS] = end

    # for row in board:
    #     print(row)

    moves, path = min_moves(board)

    if moves == -1:
        print("There is no way to win the snakes and ladders game")
        sys.exit(0)

    print(moves)
    # print(path)
    for i in range(len(path) - 1):
        if path[i + 1] - path[i] <= 6:
            print(path[i], path[i + 1])

    # To account for odd number of moves, where 100 might not be printed.
    if len(path) % 2 == 1 and 100 - path[len(path) - 2] > 6:
        print(100)


if __name__ == "__main__":
    main()
