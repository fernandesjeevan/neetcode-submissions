class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while(start<=end):
            if s[start].isalnum()==False:
                start+=1
            elif s[end].isalnum() ==False:
                end-=1
            elif s[start].lower()==s[end].lower():
                start+=1
                end-=1
            else:
                return False
        return True

            