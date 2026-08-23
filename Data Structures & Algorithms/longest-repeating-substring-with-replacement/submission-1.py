class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        str_map ={}
        max_freq = 0
        max_len = 0
        for ele in s:
            if ele in str_map:
                str_map[ele]+=1
            else:
                str_map[ele] =1
            # max_freq = max(str_map.values())
            max_freq = max(max_freq, str_map[ele])
            if right-left+1-max_freq>k:
                str_map[s[left]]-=1
                left+=1
            right+=1
            
            max_len = max(max_len,right-left)
        return max_len




