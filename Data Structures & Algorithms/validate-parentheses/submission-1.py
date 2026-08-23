class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele == '(' or ele =='{' or ele =='[':
                stack.append(ele)
            elif ele == ')':
                if stack!= [] and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ele)
            elif ele == '}':
                if stack!= [] and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(ele)
            elif ele == ']':
                if stack != []  and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(ele)
        return True if stack == [] else False