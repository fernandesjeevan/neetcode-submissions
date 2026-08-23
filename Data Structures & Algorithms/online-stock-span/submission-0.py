class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        self.arr.append(price)
        index = len(self.arr) -1
        count= 0
        if len(self.arr) ==1:
            return 1
        while index>=0:
            if self.arr[index]<=price:
                count+=1
                index-=1
            else:
                break
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)