import sys
input = sys.stdin.readline


def snail(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    start = 0
    end = n
    val = n ** 2

    while(True):
        for row in range(start, end):
            arr[row][start] = val
            val -= 1

        if val == 0:
            break

        for col in range(start + 1, end):
            arr[end - 1][col] = val
            val -= 1

        for row in range(end - 2, start - 1, -1):
            arr[row][end - 1] = val
            val -= 1

        for col in range(end - 2, start, -1):
            arr[start][col] = val
            val -= 1

        start += 1
        end -= 1

    return arr


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    arr = snail(n)

    for x in arr:
        for y in x:
            print(y, end=" ")
        print()

    try:
        for idx1, val1 in enumerate(arr):
            for idx2, val2 in enumerate(val1):
                if val2 == m:
                    print(idx1 + 1, idx2 + 1)
    except ValueError:
        print("%d is not in list" % m)
