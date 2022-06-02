# n = int(input())

# array = []
# for _ in range(n):
#     colors = list(map(str, input()))
#     array.append(colors)

# maxCount = 0  # 최대 사탕 개수를 초기화

# # 배열의 행 마다 같은 색의 사탕이 몇개 있는지 계산


# def width():
#     global maxCount

#     for k in range(n):
#         countRow = 1  # 초기 개수를 1로 초기화
#         for l in range(n - 1):
#             if array[k][l] == array[k][l + 1]:  # 만약 같은 열의 사탕의 색이 같다면
#                 countRow += 1  # 사탕 개수 1 증가
#                 # 증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
#                 maxCount = max(maxCount, countRow)
#             else:  # 만약 같은 열의 사탕 개수가 다르다면
#                 countRow = 1  # 개수를 1로 초기화


# # 배열의 열마다 같은 색의 사탕이 몇개 있는지 계산
# def height():
#     for k in range(n):
#         global maxCount

#         countColumn = 1  # 초기 개수를 1로 초기화
#         for l in range(n - 1):
#             if array[l][k] == array[l + 1][k]:  # 만약 같은 행의 사탕의 색이 같다면
#                 countColumn += 1  # 사탕 개수를 1개씩 증가시켜주고
#                 # 증가시킨 값과 최대 사탕개수를 비교하여 큰값을 대입
#                 maxCount = max(maxCount, countColumn)
#             else:  # 만약 같은 행의 색이 다르다면
#                 countColumn = 1  # 개수를 1로 초기화


# for i in range(n):
#     for j in range(n - 1):
#         # 만약 입력 받은 배열의 행의 원소가 다르다면
#         if array[i][j] != array[i][j + 1]:
#             array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
#             width()
#             height()
#             array[i][j + 1], array[i][j] = array[i][j], array[i][j + 1]
#         # 만약 입력 받은 배열의 열의 원소가 다르다면
#         if array[j][i] != array[j + 1][i]:
#             array[j][i], array[j + 1][i] = array[j + 1][i], array[j][i]
#             width()
#             height()
#             array[j + 1][i], array[j][i] = array[j][i], array[j + 1][i]

# print(maxCount)  # 색이 같은 사탕개수 최대값을 출력
import sys
read = sys.stdin.readline


def solution(n, board):
    ans = max(1, max([max(check_row(n, board, r, c), check_col(n, board, r, c))
                      for r in range(n) for c in range(n)]))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(n):
        for c in range(n):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < n and \
                        board[r][c] != board[nr][nc]:
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                    ans = max(ans, check_row(n, board, r, c),
                              check_col(n, board, r, c))
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
    return ans


def check_row(n, board, r, c):
    color = board[r][c]
    res = 1
    nr = r - 1
    # 위쪽 탐색
    while nr >= 0 and board[nr][c] == color:
        nr -= 1
        res += 1
    nr = r + 1
    # 아래쪽 탐색
    while nr < n and board[nr][c] == color:
        nr += 1
        res += 1
    return res


def check_col(n, board, r, c):
    color = board[r][c]
    res = 1
    nc = c - 1
    # 왼쪽 탐색
    while nc >= 0 and board[r][nc] == color:
        nc -= 1
        res += 1
    nc = c + 1
    while nc < n and board[r][nc] == color:
        nc += 1
        res += 1
    return res


if __name__ == "__main__":
    n = int(read())
    board = [[c for c in read().strip("\n")] for _ in range(n)]
    print(solution(n, board))
