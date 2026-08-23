class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if(num in dic.keys()):
                dic[num]+=1
            else:

                dic[num] =1
        sorted_items = sorted(dic.items(),key=lambda item: item[1], reverse=True)
        value_array = []
        for i in range(k):
            value_array.append(sorted_items[i][0])
        return value_array