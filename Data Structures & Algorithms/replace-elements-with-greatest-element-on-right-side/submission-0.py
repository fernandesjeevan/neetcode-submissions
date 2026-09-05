class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        gtr_arr = [0]*n
        maxi = arr[-1]
        for i in range(n-1,-1,-1):
            gtr_arr[i] = maxi
            maxi = max(maxi, arr[i])
            
        gtr_arr[-1] = -1
        return gtr_arr