class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return
        curr = self.root
        while True:
            if value == curr.val:
                return  # ignore duplicates
            elif value < curr.val:
                if curr.left is None:
                    curr.left = BSTNode(value)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BSTNode(value)
                    return
                curr = curr.right

    def search(self, value):
        curr = self.root
        while curr:
            if value == curr.val:
                return True
            curr = curr.left if value < curr.val else curr.right
        return False

    def inorder(self):
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(self.root)
        return res

    def preorder(self):
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(self.root)
        return res

    def postorder(self):
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                res.append(node.val)
        dfs(self.root)
        return res
