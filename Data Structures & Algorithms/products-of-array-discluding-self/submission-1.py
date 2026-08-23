class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product_map ={0:nums[0]}

        
        full_product = 1
        for num in nums:
            if num == 0:
                continue
            full_product *=num

        result = []
        for index,num in enumerate(nums):
            if num==0:
               
                flag =0
                for i in range(len(nums)):
                    print(i)
                    if(nums[i]==0 and i!=index):
                        re = 0
                        flag=1
                        break
                
                if flag==0:
                    re = full_product

            else:
                flag =0
                for i in range(len(nums)):
                    print(i)
                    if(nums[i]==0 and i!=index):
                        re = 0
                        flag=1
                        break
                
                if flag==0:
                    re = full_product//num
            result.append(re)
        return result