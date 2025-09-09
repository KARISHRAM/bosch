class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def getheight(root):
    if root is None:
        return -1
    left_height=getheight(root.left)
    right_height=getheight(root.right)
    return 1 + max(left_height,right_height)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(6)

print(getheight(root))
