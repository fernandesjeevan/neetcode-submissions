class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_set = []
        length =0
        max_len =0
        for ele in s:
            if ele in seen_set:
                max_len = max(len(seen_set),max_len)
                index =0
                temp_set =[]
                for i in range(len(seen_set)):
                    if seen_set[i] == ele:
                        index=i
                        break
                for i in range(index+1,len(seen_set)):
                    temp_set.append(seen_set[i])
                seen_set = temp_set
                seen_set.append(ele)
                max_len = max(len(seen_set),max_len)
            else:
                seen_set.append(ele)
                max_len = max(len(seen_set),max_len)
        return max_len