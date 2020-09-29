class Node(object):
    def __init__(self, data):
        self.data = data                    # Input data
        self.leftChild = None               # left Child
        self.rightChild = None              # Right Child

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)


    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)


    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)