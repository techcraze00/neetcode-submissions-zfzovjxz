class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        T = len(temperatures)
        res = []
        for l in range(T):
            count=0
            for r in range(l,T):
                if temperatures[r] > temperatures[l]:
                    count = r - l 
                    res.append(count)
                    break
                elif r == T-1:
                    res.append(0)
                    break
                
        return res