class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def k_to_last(self, k):
        current = self.head
        runner = self.head

        for _i in range(k):
            if runner is None:
                return None
            runner = runner.next

        while runner is not None:
            runner = runner.next
            current = current.next

        return current
