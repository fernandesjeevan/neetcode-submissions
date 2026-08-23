class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq ={}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.freq.get(val):
            self.freq[val]=1
        else:
            self.freq[val]+=1
           

    def pop(self) -> int:
        max_elements = []
        max_f = 0
       
        for key,value in self.freq.items():
            # print(key,value,"kv")
            if value> max_f:
                max_elements = []
                max_elements.append(key)
                max_f = value
            elif value==max_f:
                max_elements.append(key)
        #         print("have")
        # print(max_elements, "at atpo")
        ind = len(self.stack)-1
      
        while ind>=0:

            if self.stack[ind] in max_elements:
                # print(max_elements,"ythis")
                s = self.stack.pop(ind)
                self.freq[s] -=1
                # print("popped",s)
                return s
            else:
         
                ind-=1


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()