class Queue:
    def __init__(self):
        self.items = []
        self.head = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.items[self.head]
        self.head += 1
        if self.head > 32 and self.head > len(self.items) // 2:
            self.items = self.items[self.head:]
            self.head = 0
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[self.head]

    def is_empty(self):
        return self.head >= len(self.items)

    def size(self):
        return len(self.items) - self.head
