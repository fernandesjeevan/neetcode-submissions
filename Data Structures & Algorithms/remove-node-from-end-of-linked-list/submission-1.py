# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            count +=1
            dummy = dummy.next
        if count==0 or count == 1:
            return None
        pos = count - n
        count = 0
        dummy = head
        prev_node = head
        if pos==0:
            return head.next
        while count<=pos:
            if count==pos-1:
                prev_node = dummy
            if count==pos:
                prev_node.next =dummy.next
                return head
            dummy = dummy.next
            count+=1
