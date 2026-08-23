class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq ={}
        self.max_freq = 0
        self.max_ele =[]

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        if not self.freq.get(val):
            self.freq[val]=1
        else:
            self.freq[val]+=1
        if self.freq[val]>self.max_freq:
            self.max_ele =[]
            self.max_ele.append(val)
            self.max_freq = self.freq[val]
        elif self.freq[val]==self.max_freq:
            self.max_ele.append(val)



    def pop(self) -> int:
        # max_elements = []
        # max_f = 0
       
        # for key,value in self.freq.items():
        #     # print(key,value,"kv")
        #     if value> max_f:
        #         max_elements = []
        #         max_elements.append(key)
        #         max_f = value
        #     elif value==max_f:
        #         max_elements.append(key)
        #         print("have")
        # print(max_elements, "at atpo")
        ind = len(self.stack)-1
        # print(self.stack)
        # print(self.freq)
        # print(self.max_ele)
        while ind>=0:

            if self.stack[ind] in self.max_ele:
                # print(self.max_ele)
                s = self.stack.pop(ind)
                self.freq[s] -=1
                self.max_freq = self.max_freq - 1
                for key,value in self.freq.items():
                    if value> self.max_freq:
                        # print("this is max_freq",self.max_freq)
                        # print("value",value)
                        self.max_ele =[]
                        self.max_ele.append(key)
                        self.max_freq = value
                        # print("this is self.max_ele",self.max_ele)
                    elif value == self.max_freq and key not in self.max_ele:
                        self.max_ele.append(key)
                # print("popped",s)
                return s
            else:
         
                ind-=1


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()