class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1]>heights[i]:
                pop_ind, pop_height = stack.pop()
                max_area = max(max_area, pop_height*(i-pop_ind))
                start = pop_ind
            stack.append((start,heights[i]))
        print(stack)
        for i, h in stack:
            max_area = max(max_area, h*(len(heights)-i))
        return max_area
        
        
        # left_pointer = 0
        # right_pointer = 1
        # max_area = heights[0]
        # pos_stack =[[heights[0],1]]
        # for i in range(1,len(heights)):
        #     if heights[i]<heights[i-1]:
                
        #         if(pos_stack and heights[i]<pos_stack[-1][0]):
        #             print("Hi")
        #             pos_stack.pop()
        #         else:
        #             pos_stack.append([heights[i],i])
        #         for ele in pos_stack:
        #             max_area = max(max_area,ele[0]*(i+1-ele[1]))
                    
        #     else:
        #         max_area = max(heights[i],max_area)
        return max_area







