class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = nums[0]
        maj_count = 0
        for num in nums:
            if num == maj_ele:
                maj_count+=1
            else:
                maj_count-=1
            if maj_count==0:
                maj_ele = num
                maj_count =1
        return maj_ele
        # dic ={}
        # n = len(nums)
        # for num in nums:
        #     if num in dic:
        #         dic[num]+=1
        #     else:
        #         dic[num]=1
        # print(dic,n/2)
        # for key,val in dic.items():
        #     if dic[key]>n/2:
        #         return key
        # return -1