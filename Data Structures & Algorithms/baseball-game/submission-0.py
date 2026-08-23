class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rs_stack = []
        for i in range(len(operations)):
            if operations[i] == "+":
                rs_stack.append(int(rs_stack[len(rs_stack)-2])+int(rs_stack[len(rs_stack)-1]))
            elif operations[i]=="C":
                rs_stack.pop()
            elif operations[i]=="D":
                rs_stack.append(int(rs_stack[len(rs_stack)-1]*2))
            else:
                rs_stack.append(int(operations[i]))

        return sum(rs_stack)