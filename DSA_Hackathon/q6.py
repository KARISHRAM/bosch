
class slylinklistnode:
    def __init__(self, data):
        self.data=data
        self.next=None

def reverse(head):
    prev=None
    curr=head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head=head.next
    print("NULL")

head=slylinklistnode(1)
head.next=slylinklistnode(2)
head.next.next=slylinklistnode(3)

print("Original list:")
print_list(head)

head=reverse(head)

print("Reversed list:")
print_list(head)
