class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def nod(mid,weights):
            total = 0
            d =1
            for weight in weights:
                if weight+total>mid:
                    d +=1
                    total = weight
                else:
                    total+=weight
            
            return d
        
        left = max(weights)
        right = sum(weights)
        while(left<=right):
            mid = left+(right-left)//2
            nd = nod(mid,weights)
            if nd> days:
                left = mid+1
            else:
                right = mid-1
        return left

        
                 
