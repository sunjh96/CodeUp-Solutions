import sys
input = sys.stdin.readline


def sol():
    cnt = 0
    while(True):
        if not class_time:
            return cnt
        class_time.sort(key=lambda x: (x[1], x[0]))

        end = class_time[0][1]

        for x, y in class_time[1:]:
            if end <= x:
                end = y
                del class_time[class_time.index([x, y])]
        cnt += 1


if __name__ == '__main__':
    n = int(input())
    class_time = [list(map(int, input().split())) for _ in range(n)]

    print(sol())
