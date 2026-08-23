class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        count =0 
        for i in range(0,len(self.arr)):
            if self.arr[i]<=price:
                count+=1
            else:
                count = 0
        return count
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)