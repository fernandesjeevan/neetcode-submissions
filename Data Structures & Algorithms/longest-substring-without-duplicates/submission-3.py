class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_map ={}
        start_index =0
        max_len = 0
        for i in range(len(s)):
            if s[i] in seen_map:
                current_length = i -start_index
                start_index = max(start_index,seen_map[s[i]]+1)
                max_len = max(max_len,current_length)
            seen_map[s[i]] = i
            max_len = max(max_len, i-start_index+1) 
            

        return max_len
        # seen_set = []
        # length =0
        # max_len =0
        # for ele in s:
        #     if ele in seen_set:
        #         max_len = max(len(seen_set),max_len)
        #         index =0
        #         temp_set =[]
        #         for i in range(len(seen_set)):
        #             if seen_set[i] == ele:
        #                 index=i
        #                 break
        #         for i in range(index+1,len(seen_set)):
        #             temp_set.append(seen_set[i])
        #         seen_set = temp_set
        #         seen_set.append(ele)
        #         max_len = max(len(seen_set),max_len)
        #     else:
        #         seen_set.append(ele)
        #         max_len = max(len(seen_set),max_len)
        # return max_len