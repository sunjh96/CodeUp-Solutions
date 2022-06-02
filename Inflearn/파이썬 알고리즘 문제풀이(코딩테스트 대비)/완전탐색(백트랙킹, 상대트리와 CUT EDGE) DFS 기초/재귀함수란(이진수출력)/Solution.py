import sys
input = sys.stdin.readline


def di_to_bi(num):
    if num == 0:
        return
    else:
        di_to_bi(num // 2)
        print(num % 2, end='')


if __name__ == '__main__':
    num = int(input())

    di_to_bi(num)
