class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def LCA(root, n1, n2):
    if root is None:
        return None
    if root.key > n1 and root.key > n2:
        return LCA(root.left, n1, n2)
    if root.key < n1 and root.key < n2:
        return LCA(root.right, n1, n2)
    return root

root = None
root = insert(root, 20)
insert(root, 8)
insert(root, 22)
insert(root, 4)
insert(root, 12)
insert(root, 10)
insert(root, 14)

lca = LCA(root, 10, 14)
print(lca.key)