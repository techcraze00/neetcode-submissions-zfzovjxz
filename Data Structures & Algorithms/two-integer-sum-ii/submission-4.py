from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        mapper = defaultdict(set)
        n = len(numbers)
        
        for idx, num in enumerate(numbers):
            diff = target - num

            if diff not in mapper:
                mapper[num] = idx
            elif idx < n:
                # print(mapper[diff], type(mapper[diff]))
                return ([mapper[diff] + 1, idx+1])
            else:
                return([mapper[diff], idx])
        '''        
        left, right = 0 , len(numbers)-1

        while left<right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right-=1
            elif sum< target:
                left+=1
            else: return [left+1, right+1]

