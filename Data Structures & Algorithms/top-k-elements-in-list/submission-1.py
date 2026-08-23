class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        value_array = []
        result =[]
        for num in nums:
            if num in dictionary:
                dictionary[num]+=1
            else:
                dictionary[num] =1
        for value in dictionary.values():
            value_array.append(value)
        # value_array.sort(value_array.begin(),value_array.end())
        value_array.sort()
        k_freq = value_array[len(value_array)-k]
        for key,value in dictionary.items():
            if value>=k_freq:
                result.append(key)    
            
        return result