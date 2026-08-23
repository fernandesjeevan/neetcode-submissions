class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while(left<=right):
            nh = 0
            mid = left + (right-left)//2
            for pile in piles:
                if pile%mid==0:
                    nh+=pile//mid
                else:
                    nh+= pile//mid +1
            if nh> h:
                left = mid+1
            elif nh<h:
                right = mid-1
            else:
                
                right = mid-1
           
        return left
            
        
