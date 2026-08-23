class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        left = 0
        t_map ={}
        for i in range(len(t)):
            t_map[t[i]] = t_map.get(t[i],0)+1
        have, need = 0, len(t_map.values())
        s_map = {}
        l,r = 0,0
        min_len = float("infinity")
        min_str = ""
        for right in range(len(s)):
            if s[right] in t_map:
                s_map[s[right]] = s_map.get(s[right],0)+1
            if s[right] in t_map and s_map[s[right]] ==t_map[s[right]]:
                have+=1
            while have==need:                
                if min_len>right-left+1:
                    min_len = right-left+1
                    min_str = s[left:right+1]
                if s[left] in t_map:
                    s_map[s[left]]-=1
                if s[left] in t_map and s_map[s[left]]<t_map[s[left]]:
                    have-=1
                left+=1
        return min_str

        