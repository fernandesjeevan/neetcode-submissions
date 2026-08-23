class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        full_product = 1
        zero_counter =0
        for num in nums:
            if num == 0:
                zero_counter+=1
            else:
                full_product *=num
        print(zero_counter)
        result = []
        for index,num in enumerate(nums):
            if zero_counter>1:
                re = 0
            elif num==0:
                re = full_product
            elif num!=0 and zero_counter==1:
                re =0
            else:    
                re = full_product//num
            result.append(re)
        return result