# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        secondHead = slow.next
        prev = None
        slow.next = None

        while secondHead:
            temp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = temp
        
        firstHead, secondHead = head, prev

        while secondHead:
            temp1, temp2 = firstHead.next, secondHead.next
            firstHead.next  = secondHead
            secondHead.next = temp1
            firstHead, secondHead = temp1, temp2
