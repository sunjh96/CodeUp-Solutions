import sys
import heapq
input = sys.stdin.readline


def sol():
    heap = []
    ans = []

    for _ in range(int(input())):
        n = int(input())
        if n == 0:
            if not heap:
                ans.append(0)
            else:
                ans.append(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap, (-n, n))

    print(*ans, sep='\n')


if __name__ == '__main__':
    sol()
