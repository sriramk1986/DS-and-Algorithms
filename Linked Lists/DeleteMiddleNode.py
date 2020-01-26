class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, node):
        node.value = node.next.value
        node.next = node.next.next
