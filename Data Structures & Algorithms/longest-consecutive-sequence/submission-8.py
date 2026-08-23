class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_cons_seq = 0
        cons_seq = 1
        if(len(nums)==1):
            max_cons_seq = 1
        for i in range(len(nums)-1):
            
            if nums[i] == nums[i+1]:
                max_cons_seq = max(max_cons_seq, cons_seq)
                continue
            elif nums[i]+1==nums[i+1]:
                cons_seq +=1
                max_cons_seq = max(max_cons_seq,cons_seq)
            else:
                cons_seq = 1
                max_cons_seq = max(max_cons_seq,cons_seq)
        return max_cons_seq

            
