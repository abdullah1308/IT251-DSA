import sys


def main():
    if len(sys.argv) != 2:
        return

    file = open(sys.argv[1], 'r')

    pattern = file.readline().strip()
    text = file.readline().strip()

    # print(pattern)
    # print(text)

    occurrences = findOccurrences(pattern, text)

    if len(occurrences) == 0:
        print("Pattern not found.")
        return

    for occur in occurrences:
        print(occur, end=" ")
    print()

def findOccurrences(pattern, text):
    lps = convertToLps(pattern)
    occurrences = []

    textIdx = 0
    patIdx = 0

    while textIdx < len(text):
        if text[textIdx] == pattern[patIdx]:
            textIdx += 1
            patIdx += 1
        else:
            if patIdx != 0:
                patIdx = lps[patIdx - 1]
            else:
                textIdx += 1

        if patIdx == len(pattern):
            occurrences.append(textIdx - patIdx)
            patIdx = 0

    return occurrences


def convertToLps(pattern):
    lps = [0 for _ in range(len(pattern))]

    matchIdx = 0
    patIdx = 1

    while patIdx < len(pattern):
        if pattern[matchIdx] == pattern[patIdx]:
            lps[patIdx] = matchIdx + 1
            matchIdx += 1
            patIdx += 1
        else:
            if matchIdx == 0:
                lps[patIdx] = 0
                patIdx += 1
            else:
                matchIdx = lps[matchIdx - 1]

    return  lps

if __name__ == '__main__':
    main()