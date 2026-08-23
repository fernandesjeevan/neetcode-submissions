class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                substr =""
                nums = ""
                while stack[-1]!="[":

                    substr = stack.pop()+substr
                stack.pop()
                while stack and stack[-1].isdigit():
                    nums = stack[-1]+nums
                    stack.pop()
                res = int(nums)*substr
                stack.append(res)
        return "".join(stack)
                

        
        
        # stack =[]
        # for ss in s:
        #     if ss == ']':
                
        #         string = ""
        #         while(stack):
        #             if stack and stack[-1].isalpha():
        #                 string+=stack[-1]
        #                 stack.pop()
        #             elif stack and stack[-1].isalnum() and isinstance(stack[-1].isalnum(),int):
                        
        #                 stack.pop()
        #                 for i in range(int(stack[-1])):
        #                     stack.append(int(stack[-1]*string))
        #             else:
        #                 stack.pop()
        #         # temp =[]
        #         # while stack:
        #         #     if stack[-1].isalpha():
        #         #         temp.append(stack[-1])
                        
        #         #         stack.pop()
        #         #     elif stack[-1].isalnum() and isinstance(stack[-1],int):
        #         #         t = temp.pop()
        #         #         snum = stack.pop()
        #         #         print(stack)
        #         #         for i in range(snum):
        #         #             stack.append(t)
        #         #             print(stack)
        #         #         break
        #         #     else:
        #         #         s
                        
        #     else:
        #         stack.append(ss)
               
        # return str(stack)
