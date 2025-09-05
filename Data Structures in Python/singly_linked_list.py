class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def delete(self, data):
        prev, curr = None, self.head
        while curr:
            if curr.data == data:
                if prev is None:
                    self.head = curr.next
                    if curr is self.tail:
                        self.tail = None
                else:
                    prev.next = curr.next
                    if curr is self.tail:
                        self.tail = prev
                self.size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def display(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        s = " -> ".join(vals) if vals else "<empty>"
        print(s)
        return s
