class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.itmes):
            print("Queue is empty!")
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def isEmpty(self):
        if self.front_index == len(self.itmes):
            print("Queue is empty!")
        else:
            return len(self.itmes) - self.front_index

    def front(self):
        return self.items[self.front_index]

    def len(self):
        return len(self.itmes) - self.front_index
