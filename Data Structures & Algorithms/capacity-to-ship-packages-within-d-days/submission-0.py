class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def nod(mid,weights):
            sm = 0
            d = 1
            i=0
            while i<len(weights):
                if sm+weights[i]>mid:   
                    if weights[i]>mid:
                        return days+1                     
                    d+=1
                    sm=0
                   
                   
                else:
                    sm+=weights[i]
                    i+=1
            return d
        
        left = 1
        right = sum(weights)
        while(left<=right):
            mid = left+(right-left)//2
            nd = nod(mid,weights)
            if nd> days:
                left = mid+1
            else:
                right = mid-1
        return left

        
                 
