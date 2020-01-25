class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def removeNode(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.removeKeyBindings(node)

    def removeKeyBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nextNode = node.next
            if node.value == value:
                self.removeNode(node)
            node = nextNode

    def insertBeforeNode(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.removeNode(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    def insertAfterNode(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.removeNode(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBeforeNode(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfterNode(self.tail, node)

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        count = 1
        currentNode = None
        while node is not None and count != position:
            count += 1
            node = node.next
        if node is not None:
            self.insertBeforeNode(currentNode, nodeToInsert)

    def append(self, value):
        node = Node(value)

        if self.tail is None:
            self.setTail(node)
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def removeDuplicates(self):
        valueHash = {}
        if self.head is None:
            return
        node = self.head
        while node is not None:
            nextNode = node.next
            if node.value in valueHash:
                self.removeNode(node)
            else:
                valueHash[node.value] = True
            node = nextNode

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


llist = DoublyLinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

llist.removeDuplicates()
llist.print_list()

