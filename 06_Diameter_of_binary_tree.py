class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter(root):
    diameter_val = [0]

    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter_val[0] = max(diameter_val[0], left_height + right_height + 1)
        return 1 + max(left_height, right_height)

    height(root)
    return diameter_val[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameter(root))