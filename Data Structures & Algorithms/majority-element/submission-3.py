class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic ={}
        n = len(nums)
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        print(dic,n/2)
        for key,val in dic.items():
            if dic[key]>n/2:
                return key
        return -1