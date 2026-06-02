class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_min(root):
    current = root

    while current.left:
        current = current.left

    return current.key


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Minimum value:", find_min(root))