class Solution:
    def validPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        del_flag = 0
        def isPalindrome(lp,rp,s):
            while lp<rp:
                if s[lp] ==s[rp]:   
                    lp+=1
                    rp-=1

                else:
                    return False
            return True

      
        while lp<rp:
            print(s[lp],s[rp])
            if s[lp] ==s[rp]:   
                lp+=1
                rp-=1

            else:
                return isPalindrome(lp+1,rp,s) or isPalindrome(lp,rp-1,s)
                
                    
        
        return True