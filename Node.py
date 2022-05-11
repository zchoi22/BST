#Node class in Python
#Author: Ms. Hellman
#Transcribed? Zion Choi
#OMH

class Node:
    #constructor, has option values for left and right nodes
    def __init__(self, key, value, size=1, left=None, right=None):
        self.key = key
        self.value = value
        self.size = size
        self.left = left
        self.right = right

    #To string method
    def toString(self):
        return "Node{" + "key=" + self.key + ", value=" + self.value + "}"

    #getters and setters for all variables
    def getKey(self):
        return self.key

    def setKey(self, key):
        self.key = key

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getSize(self):
        return self.size

    def setSize(self, size):
        self.size = size