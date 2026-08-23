class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for s in strs: 
            encoded_string +=s
            encoded_string +="\t"   
        print(encoded_string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strings: List[str] = []
        brk_cnt = 0 
        for i in range (0,len(s)):
            if(s[i]=='\t'):

                dc_string = s[brk_cnt:i]
                decoded_strings.append(dc_string)
                brk_cnt =i+1
        return decoded_strings


