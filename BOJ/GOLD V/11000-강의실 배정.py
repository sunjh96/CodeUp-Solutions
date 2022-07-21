import sys
input = sys.stdin.readline


def sol():
    cnt = 0
    class_time.sort(key=lambda x: (x[1], x[0]))
    end = class_time[0][1]

    while(True):

        del class_time[0]
        for idx, (x, y) in enumerate(class_time):
            if end <= x:
                end = y
                del class_time[idx]

        cnt += 1

        if len(class_time) <= 1:
            return cnt

        end = class_time[0][1]

if __name__ == '__main__':
    n = int(input())
    class_time = [list(map(int, input().split())) for _ in range(n)]

    if n == 1:
        print(1)
    else:
        print(sol())


# 1 3
# 2 4
# 3 5
# 6 9
# 7 8
# 9 10
