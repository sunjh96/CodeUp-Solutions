import sys


class Stack:
    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, val):
        self.items.append(val)
        if not self.min_items or val < self.min_items[-1]:
            self.min_items.append(val)

    def pop(self):
        try:
            val = self.items.pop()
            if val == self.min_items[-1]:
                self.min_items.pop()

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

    def __min__(self):
        return self.min_items.pop()


n, k = map(int, sys.stdin.readline().split())
n = str(n)
arr = list(n)

stack = Stack()
i = 0
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
