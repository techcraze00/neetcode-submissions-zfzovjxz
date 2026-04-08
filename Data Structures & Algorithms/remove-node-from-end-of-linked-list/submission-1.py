# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # creating circular ll
        if not head or not head.next: return None
        dummy = ListNode(0, head)
        curr = dummy
        tail = head

        for i in range(n):
            tail = tail.next

        while tail :
            curr = curr.next
            tail = tail.next
        # print([curr.val, tail.val])
        curr.next = curr.next.next
        # if curr.next.next:
        #     curr = curr.next.next
        # else:
        #     curr.next = tail
        return dummy.next
