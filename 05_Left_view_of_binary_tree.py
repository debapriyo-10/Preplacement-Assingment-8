class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftView(root):
    max_level = [0]
    result = []
    
    def leftViewUtil(node, level):
        if not node:
            return
        if max_level[0] < level:
            result.append(node.data)
            max_level[0] = level
        leftViewUtil(node.left, level+1)
        leftViewUtil(node.right, level+1)
    
    leftViewUtil(root, 1)
    return result

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

print(*leftView(root))