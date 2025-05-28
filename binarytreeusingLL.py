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

def print_preorder(tree):
    if tree:
        print(tree.data)
        print_preorder(tree.left)
        print_preorder(tree.right)

def print_inorder(tree):
    if tree:
        print_inorder(tree.left)
        print(tree.data)
        print_inorder(tree.right)

def print_postorder(tree):
    if tree:
        print_postorder(tree.left)
        print_postorder(tree.right)
        print(tree.data)

def search(tree, val):
    if tree is None:
        return None
    
    if val < tree.data:
        return search(tree.left, val)
    elif val > tree.data:
        return search(tree.right, val)
    else:
        return tree  # Found it

def delete_tree(tree):
    
    if tree:
        delete_tree(tree.left)
        delete_tree(tree.right)
        tree.left = None
        tree.right = None

# ---------- Main Execution Section ----------

root = None

# Insert values
root = insert(root, 9)
root = insert(root, 4)
root = insert(root, 15)
root = insert(root, 6)
root = insert(root, 12)
root = insert(root, 17)
root = insert(root, 2)

# Print traversals
print("Pre Order Display")
print_preorder(root)

print("In Order Display")
print_inorder(root)

print("Post Order Display")
print_postorder(root)

# Search for a node
found = search(root, 4)
if found:
    print(f"Searched node = {found.data}")
else:
    print("Data not found in tree.")

# Delete all nodes
delete_tree(root)
root = None

