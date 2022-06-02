import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            val = self.items.pop()
            return val
        except IndexError:
            print("Stack is Empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):
        return len(self.items)


n, k = map(int, sys.stdin.readline().split())
n = str(n)
arr = list(map(int, n))

stack = Stack()
cnt = 0

for i in range(len(arr)):
    if not stack or stack.top() >= arr[i]:
        if stack.__len__() == len(arr) - k:
            continue
        stack.push(arr[i])
    else:
        while(True):
            if not stack or stack.top() >= arr[i] or cnt == k:
                break
            stack.pop()
            cnt += 1
        stack.push(arr[i])

print(*stack.items, sep='')
