# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        t1 = 1
        t2 = 1
        while l1:
            n1 += l1.val*t1
            t1 = t1*10
            l1 = l1.next
        while l2:
            n2 += l2.val*t2
            
            t2 = t2*10
            l2 = l2.next
        res = n1+n2
        dummy = ListNode()
        curr = dummy
        while res:
            dig = res%10
           
            curr.val = dig
            res = res//10
            if res!=0:
                curr.next = ListNode()
                curr = curr.next
            

        return dummy
        # rev = 0
        # n = 1
        
        # while res:
        #     dig = res%10
        #     rev = rev*10 +dig
            
          
        #     res = res//10
        # dummy = listNode()
        return l1


        