class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(tree, val):
    if tree is None:
        return Node(val)
    if val < tree.data:
        tree.left = insert(tree.left, val)
    elif val > tree.data:
        tree.right = insert(tree.right, val)
    return tree

def print_inorder(tree):
    if tree:
        print_inorder(tree.left)
        print(tree.data, end=' -> ')
        print_inorder(tree.right)


root = None
for val in [9, 4, 15, 6, 12, 17, 2]:
    root = insert(root, val)

print("In-order Traversal:")
print_inorder(root)
print("NULL") 
