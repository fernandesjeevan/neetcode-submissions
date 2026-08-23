class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res_array = []
        for i in range(0,len(asteroids)):
            if res_array == []:
                res_array.append(asteroids[i])
            elif asteroids[i] < 0 and res_array[-1]>0:
                ast_exp=0
                while res_array!=[] and res_array[-1]>0:
                    if abs(asteroids[i])> abs(res_array[-1]):
                        res_array.pop()
                       
                    elif abs(asteroids[i]) == abs(res_array[-1]):
                        res_array.pop()
                        ast_exp = 1
                        break
                    else:
                        ast_exp =1
                        break
                if ast_exp !=1:
                    res_array.append(asteroids[i])
    
            else:
                res_array.append(asteroids[i])
        return res_array