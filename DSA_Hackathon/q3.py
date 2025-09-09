class slylinklistnode:
    def __init__(self, data):
        self.data=data
        self.next=None

def create_linked_list(values):
    if not values:
        return None
    head=slylinklistnode(values[0])
    current=head
    for value in values[1:]:
        current.next=slylinklistnode(value)
        current=current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data)
        head=head.next

values=[1, 2, 3, 4, 5]
head=create_linked_list(values)
print_linked_list(head)
