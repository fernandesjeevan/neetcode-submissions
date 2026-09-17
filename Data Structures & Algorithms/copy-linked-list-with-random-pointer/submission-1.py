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
        dummy = Node(0)
        dummy1 = dummy
        cur = head
        map1 = {}
        while cur:
            dummy.next = Node(cur.val)
            map1[cur] = dummy.next
            cur = cur.next
            dummy = dummy.next
            
        cur = head
        dummy = dummy1
        while cur:
            dummy1.next.random = map1.get(cur.random)
            cur = cur.next
            dummy1 = dummy1.next
        return dummy.next
