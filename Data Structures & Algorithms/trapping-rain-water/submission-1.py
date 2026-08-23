class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        max_height_l, max_height_r = height[l],height[r]
        res =0
        while l<r:
            if max_height_l<= max_height_r:
                
                l+=1
                max_height_l = max(max_height_l,height[l])
                res += max_height_l - height[l]
            else:
                r-=1
                max_height_r = max(max_height_r, height[r])
                res += max_height_r - height[r]
        return res  
                