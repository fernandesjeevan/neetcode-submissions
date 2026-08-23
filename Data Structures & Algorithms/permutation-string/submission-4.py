class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        if s1_length>s2_length:
            return False
        left =0
        right = s1_length
        sorted_s1 = sorted(s1)
    
        for i in range(s2_length-s1_length+1):
            check_string = sorted(s2[i:i+s1_length])
            print(i,check_string,sorted_s1)
            if sorted_s1 ==check_string:
                return True
        return False
