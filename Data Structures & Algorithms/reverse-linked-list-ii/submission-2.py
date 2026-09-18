# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node = None
        right_node = None
        left_prev_node = None
        right_next_node = None
        index = 1
        prev,cur = None,head
        if left==right:
            return head

        while cur:
            
            if index==left:
                left_node = cur
                left_prev_node = prev
                if prev is not None:
                    prev.next =None
            elif index==right:
                right_node =cur
                right_next_node = cur.next
                right_node.next = None
                
                
            prev = cur
            cur = cur.next
            index+=1
        prev,cur = None,left_node
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        if left_prev_node:
            left_prev_node.next = prev
        else:
            head = prev
        cur = prev
        while cur.next:
           
            cur = cur.next
        if cur is not None:
            cur.next = right_next_node
    
        return head






        # prev,cur = None, head
        # tracker = head
        # right_next = None
        # right_node = None
        # for i in range(right+1):
        #     if i==right:
        #         right_next = tracker.next
        #         tracker.next = None
        #         break
        # while cur:
        #     nxt = head.next
        #     head.next = prev
        #     cur = head.next
        #     prev = head
        # return prev
            
            
        
        
