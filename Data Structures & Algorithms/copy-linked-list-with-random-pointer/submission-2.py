"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mpp = {None:None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            mpp[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = mpp[cur]
            copy.next = mpp[cur.next]
            copy.random = mpp[cur.random]
            cur=cur.next
        return mpp[head]
