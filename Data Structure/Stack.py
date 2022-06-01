class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

# 최솟값 출력 가능


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
