class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right =x
        mid = left +(right-left)//2
        while(left<=right):
            
            if(mid*mid==x):
                return mid
            elif(mid*mid>x):
                right = mid-1
            else:
                left = mid+1
            mid = left +(right-left)//2
        return left-1