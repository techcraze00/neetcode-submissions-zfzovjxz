class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        maper =defaultdict()

        for idx, n in enumerate(numbers):
            diff = target - n
            
            if diff in maper:
                return [maper[diff]+1,idx+1]
            
            maper[n] = idx
        