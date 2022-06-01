import sys


class Stack():
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is Empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")

    def __len__(self):
        return len(self.items)


arr = sys.stdin.readline().strip()
stack = Stack()
cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.push(arr[i])
    else:
        if arr[i - 1] == '(':
            stack.pop()
            cnt += stack.__len__()
        else:
            stack.pop()
            cnt += 1

print(cnt)
