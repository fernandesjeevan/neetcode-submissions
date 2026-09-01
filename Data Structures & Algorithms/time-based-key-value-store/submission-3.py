class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
           
            self.dic[key] =[{timestamp:value}]
        else:
           
            self.dic[key].append({timestamp:value})

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        else:
            res = ""
            item = self.dic[key]
            left =0
            right = len(item)-1
            while(left<=right):
                mid = left+(right-left)//2
                mid_item = item[mid]            
                for k,v in mid_item.items():
                    if k==timestamp:
                        return v
                    elif k<timestamp:
                        res = v
                        left=mid+1
                    else:
                        right=mid-1      
            return res
                
                    
                
                

            # print(self.dic[key][0],self.dic[key][-1])
            # for item in self.dic[key]:
            #     print(item)
                # for k,v in item.items():
                #     if k< timestamp:
                #         res = v
                #     elif k ==timestamp:
                #         return v
                #     else:
                #         return res
            return res

                    