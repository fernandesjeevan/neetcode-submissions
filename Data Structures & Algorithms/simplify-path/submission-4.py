class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "" or p==".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
        # stack = []
        # st = ""
        # for i in range(len(path)):
        #     if not st and path[i]=='/':
        #         # st+=path[i]
        #         continue
        #     elif st and path[i]=='/':
        #         # st+=path[i]
        #         stack.append(st)
        #         st= ""
        #     else: 
        #         st+=path[i]
        # stack.append(st)
        # i = len(stack)-1
        # print(stack)
        # while(i>=0):
        #     print(i)
        #     if len(stack)>1 and stack[i] =='..':
        #         print(stack)
        #         stack.pop(i)
        #         stack.pop(i-1)
        #     elif stack[i]=="..":
        #         stack.pop()
        #     i-=1
        # res= "/"
        # for ele in stack:
            
        #     res+=ele
        #     res+="/"
        # print(len(res))       
        # if len(res)==1:
        #     return res
        # else:
        #     return res[:-1]
        # # for p in path:

        #     if p =='/':
        #         if stack and stack[-1] =='/':
        #             continue
        #         else:
        #             stack.append(p)

        #     elif p=='.':
        #         if stack and stack[-1]!='.':
        #             stack.append(p)
        #         elif len(stack)>1 and stack[-1] =='.':
        #             if stack[-2] =='.':
        #                 stack.append(p)
        #             else:
        #                 slash_count =0
        #                 while(slash_count<2 and stack):
        #                     s = stack.pop()
        #                     print(s)
        #                     if s=='/':
                                
        #                         slash_count+=1
        #                         print(slash_count)
                       
                

        #     else:
        #         stack.append(p)   
        # res = ""    
        # for ele in stack:
        #     if ele =='.':
        #         continue
        #     res+=ele

       
        # return res