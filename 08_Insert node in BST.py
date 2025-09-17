class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if not (min_val < root.data < max_val):
        return False
    return (isBST(root.left, min_val, root.data) and
            isBST(root.right, root.data, max_val))

root = Node(10)
root.left = Node(5)
root.right = Node(20)

print("Yes" if isBST(root) else "No")