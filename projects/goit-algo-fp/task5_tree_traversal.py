import uuid

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id,
            color=node.color,
            label=node.val
        )

        if node.left:
            graph.add_edge(node.id, node.left.id)

            l = x - 1 / 2 ** layer

            pos[node.left.id] = (l, y - 1)

            add_edges(
                graph,
                node.left,
                pos,
                x=l,
                y=y - 1,
                layer=layer + 1
            )

        if node.right:
            graph.add_edge(node.id, node.right.id)

            r = x + 1 / 2 ** layer

            pos[node.right.id] = (r, y - 1)

            add_edges(
                graph,
                node.right,
                pos,
                x=r,
                y=y - 1,
                layer=layer + 1
            )

    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()

    pos = {tree_root.id: (0, 0)}

    tree = add_edges(tree, tree_root, pos)

    colors = [
        node[1]["color"]
        for node in tree.nodes(data=True)
    ]

    labels = {
        node[0]: node[1]["label"]
        for node in tree.nodes(data=True)
    }

    plt.figure(figsize=(8, 5))

    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors
    )

    plt.show()


def dfs(root):

    stack = [root]

    visited = []

    while stack:
        current = stack.pop()

        visited.append(current)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return visited


def bfs(root):

    queue = deque([root])

    visited = []

    while queue:
        current = queue.popleft()

        visited.append(current)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return visited

def generate_colors(n):

    colors = []

    for i in range(n):

        blue = 255
        gray = 40 + int(140 * i / (n - 1))

        colors.append(
            f"#{gray:02x}{gray:02x}{blue:02x}"
        )

    return colors


root = Node(0)

root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)

root.right = Node(1)
root.right.left = Node(3)


dfs_nodes = dfs(root)

colors = generate_colors(len(dfs_nodes))

for node, color in zip(dfs_nodes, colors):
    node.color = color

print("DFS:")

for node in dfs_nodes:
    print(node.val)

draw_tree(root)

bfs_nodes = bfs(root)

colors = generate_colors(len(bfs_nodes))

for node, color in zip(bfs_nodes, colors):
    node.color = color

print("\nBFS:")

for node in bfs_nodes:
    print(node.val)

draw_tree(root)




