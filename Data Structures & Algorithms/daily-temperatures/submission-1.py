class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
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
        '''

        result = [0]* len(temperatures)
        stack = [] # pair of temp:index

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = idx - stackIdx
            stack.append([temp,idx])
        return result
