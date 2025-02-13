def deleteDuplicates(head):
    """
    :param head: ListNode
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
    :return: ListNode
    """
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head