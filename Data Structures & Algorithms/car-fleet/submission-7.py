class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_zip = sorted(list(zip(position,speed)))
        time_taken = []
        for key,value in sorted_zip:
            time = (target -key)/value
            time_taken.append(time)
        i = len(time_taken)-1
        fleet = [time_taken[i]]
        i-=1
        while(i>=0):
            if(time_taken[i]>fleet[-1]):
                fleet.append(time_taken[i])
            i-=1
        

        
        
        return len(fleet)


        