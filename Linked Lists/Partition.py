class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def partition(self, head, n):
    beforeStart = ListNode(None)
    beforeEnd = ListNode(None)
    afterStart = ListNode(None)
    afterEnd = ListNode(None)

    while head:
        if head.val < n:
            if beforeStart.val is None:
                beforeStart = head
                beforeEnd = head
            else:
                beforeEnd.next = head
                beforeEnd = beforeEnd.next
        else:
            if afterStart.val is None:
                afterStart = head
                afterEnd = head
            else:
                afterEnd.next = head
                afterEnd = afterEnd.next
        head = head.next
    afterEnd.next = None

    beforeEnd.next = afterStart
    return beforeStart
