class Btnode:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

root = None
temp = None
t1 = None
t2 = None
flag = 1

def create():
    global temp
    data = int(input("Enter data of node to be inserted: "))
    temp = Btnode(data)

def search(t):
    global temp
    if temp.value > t.value:
        if t.r is not None:
            search(t.r)
        else:
            t.r = temp
    elif temp.value < t.value:
        if t.l is not None:
            search(t.l)
        else:
            t.l = temp

def insert():
    global root, temp
    create()
    if root is None:
        root = temp
    else:
        search(root)

def inorder(t):
    if root is None:
        print("No elements in a tree to display")
        return
    if t.l is not None:
        inorder(t.l)
    print(t.value, end=" -> ")
    if t.r is not None:
        inorder(t.r)

def preorder(t):
    if root is None:
        print("No elements in a tree to display")
        return
    print(t.value, end=" -> ")
    if t.l is not None:
        preorder(t.l)
    if t.r is not None:
        preorder(t.r)

def postorder(t):
    if root is None:
        print("No elements in a tree to display")
        return
    if t.l is not None:
        postorder(t.l)
    if t.r is not None:
        postorder(t.r)
    print(t.value, end=" -> ")

def search1(t, data):
    global t1
    if data > t.value:
        t1 = t
        search1(t.r, data)
    elif data < t.value:
        t1 = t
        search1(t.l, data)
    else:  # data == t.value
        delete1(t)

def delete1(t):
    global root, t1, t2, flag

    # Leaf node
    if t.l is None and t.r is None:
        if t1.l == t:
            t1.l = None
        else:
            t1.r = None
        return

    # Node with only left child
    elif t.r is None:
        if t1 == t:
            root = t.l
            t1 = root
        elif t1.l == t:
            t1.l = t.l
        else:
            t1.r = t.l
        return

    # Node with only right child
    elif t.l is None:
        if t1 == t:
            root = t.r
            t1 = root
        elif t1.r == t:
            t1.r = t.r
        else:
            t1.l = t.r
        return

    # Node with two children
    elif t.l is not None and t.r is not None:
        t2 = root
        if t.r is not None:
            k = smallest(t.r)
            flag = 1
        else:
            k = largest(t.l)
            flag = 2
        search1(root, k)
        t.value = k

def smallest(t):
    global t2
    t2 = t
    if t.l is not None:
        t2 = t
        return smallest(t.l)
    else:
        return t.value

def largest(t):
    if t.r is not None:
        return largest(t.r)
    else:
        return t.value

def delete():
    global root, t1
    if root is None:
        print("No elements in a tree to delete")
        return
    data = int(input("Enter the data to be deleted: "))
    t1 = root
    search1(root, data)

def main():
    while True:
        print("\nOPERATIONS ---")
        print("1 - Insert an element into tree")
        print("2 - Delete an element from the tree")
        print("3 - Inorder Traversal")
        print("4 - Preorder Traversal")
        print("5 - Postorder Traversal")
        print("6 - Exit")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            delete()
        elif ch == 3:
            inorder(root)
            print()
        elif ch == 4:
            preorder(root)
            print()
        elif ch == 5:
            postorder(root)
            print()
        elif ch == 6:
            print("Exiting...")
            break
        else:
            print("Wrong choice, Please enter correct choice")

if __name__ == "__main__":
    main()
