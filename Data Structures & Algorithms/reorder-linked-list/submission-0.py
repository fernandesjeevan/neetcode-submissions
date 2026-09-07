# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            count+=1
        mid_point = (count+1)//2
        n=0
        dummy = head
        mid_point_node = ListNode()
        prev_node = ListNode()
        for i in range(0,mid_point):
            prev_node = dummy
            dummy = dummy.next
        
        mid_point_node = dummy
        county = 0
        prev_node.next = None
        prev_node = None
        while mid_point_node:
        
            nxt = mid_point_node.next
            mid_point_node.next = prev_node
            prev_node = mid_point_node
            mid_point_node = nxt
        
        while head and prev_node:
            nxt = head.next
            second_nxt = prev_node.next
            head.next = prev_node
            prev_node.next = nxt
            head = nxt
            prev_node = second_nxt
        
        
    
                

        
        
        
   
           
            
            
        # while prev_node.next:
        #     print(prev_node)

        # while mid_point_node:
        #     nxthead = head.next
        #     altnext = mid_point_node.next
        #     head.next = mid_point_node
        #     mid_point_node = altnext
        #     head  = nxthead
        
            