# Binary-tree-programs

hello welcome to my repo
today we are going to see two programs
both the programs are in python language

1) Binary tree using linked list:


This program is performing common operations on a Binary Search Tree (BST):

Insert:
Adds a new value to the tree such that:
Left child < parent
Right child > parent

Traversal Functions:
print_preorder: Root → Left → Right
print_inorder: Left → Root → Right
print_postorder: Left → Right → Root

Search:
Looks for a value in the BST and returns a pointer to the node if found.

Delete Tree:
Frees all dynamically allocated memory for nodes.


2) Binary search tree


Interactive menu program that allows the user to:
Insert nodes into the BST.
Delete nodes from the BST.
Traverse and display the BST in Inorder, Preorder, and Postorder.
Exit the program.


Insertion
The user inputs a value.
A new node is created.
The program finds the correct spot in the tree (left for smaller, right for larger) to insert the node.


Traversal
Inorder: Left subtree → Node → Right subtree (prints sorted values).
Preorder: Node → Left subtree → Right subtree.
Postorder: Left subtree → Right subtree → Node.

Deletion
The user inputs a value to delete.
The program searches for that node.
Once found, it deletes the node.



smallest(): Finds the minimum value node in a subtree.
largest(): Finds the maximum value node in a subtree.
