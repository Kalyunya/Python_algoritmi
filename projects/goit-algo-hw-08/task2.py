class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def sum_tree(root):
    if root is None:
        return 0

    return root.key + sum_tree(root.left) + sum_tree(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Sum:", sum_tree(root))