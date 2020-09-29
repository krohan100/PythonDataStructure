class Node(object):
    #Constructor
    def __init__(self,data):
        self.data = data            # Data to be stored
        self.nextNode = None        # Pointer to the next node; Initialized to "None"


# Linked List head (root node) and size
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self, data):
        self.size += 1
        newNode = Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        return 'Node {} added to head of Linked List'.format(data)

    def insertEnd(self, data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
        return 'Node {} added to end of Linked List'.format(data)

    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    def linkedListSize(self):
        return self.size

    def removeNode(self, data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
        return 'Node {} Removed from Linked List'.format(data)

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d ' % actualNode.data)
            actualNode = actualNode.nextNode

# main method
if __name__ == '__main__':
    linked_list = LinkedList()
    print(linked_list.insertStart(12))
    print(linked_list.insertEnd(16))
    linked_list.traverseList()