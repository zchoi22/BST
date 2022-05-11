#BST
#Author Zion Choi
#OMH

from Node import Node

class BST:

    def __init__(self, root =None):
        self.root = root

    def size(self):
        return self.private_size(self.root)

    def private_size(self, root):
        if root == None:
            return 0
        return root.getSize() + self.private_size(root.getLeft()) + self.private_size(root.getRight())

    def isEmpty(self):
        return self.size() == 0

    def put(self, key, value):
        self.root = self.private_put(self.root, key, value)

    def private_put(self, root, key, value):
        if root == None:
            return Node(key, value)
        if key > root.getKey():
            root.setRight(self.private_put(root.getRight(), key, value))
        else:
            root.setLeft(self.private_put(root.getLeft()), key, value)
        return root

    def get(self, key):
        return self.private_get(self.root, key)

    def private_get(self, root, key):
        if root == None:
            return None
        if key > root.getKey():
            return self.private_get(root.getRight(), key)
        elif key < root.getKey():
            return self.private_get(root.getLeft(), key)
        return root.getValue()

    def contains(self, key):
        return self.get(key) != None

    def remove(self, key):
        value = self.get(key)
        root = self.private_remove(self.root, key)
        return value

    def private_remove(self, root, key):
        if root == None: return None
        i = key - root.getKey()
        if i < 0:
            root.setLeft(self.private_remove(root.getLeft(), key))
        elif i > 0:
            root.setRight(self.private_remove(root.getRight(), key))
        else:
            if root.getRight() == None: return root.getLeft()
            if root.getLeft() == None: return root.getRight()
            min = self.private_min(root.getRight())
            min.setLeft(root.getLeft())
            root = root.getRight()
        root.setSize(self.private_size(root.getRight()), self.private_size(root.getLeft()) +1)
        return root

    def min(self):
        return self.private_min(self.root).getKey()

    def private_min(self, root):
        if root.getLeft() == None:
            return root
        return self.private_min(root.getLeft())

    def max(self):
        return self.private_max(self.root).getKey()

    def private_max(self, root):
        if root.getRight() == None:
            return root
        return self.private_max(root.getRight())

    def toString(self):
        temp = self.private_toString(self.root)[0:-2]
        return "{" + temp + "}"

    def private_toString(self, root):
        if root == None: return ""
        return self.private_toString(root.getLeft()) + root.getKey() + "=" + root.getValue() + ", " + self.private_toString(root.getRight())