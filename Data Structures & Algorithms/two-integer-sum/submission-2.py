class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inMapper={}
        # print(enumerate(nums))
        
        for idx, num in enumerate(nums):
            diff=target-num
            if diff in inMapper:
                return [inMapper[diff], idx]
            
            inMapper[num] = idx
        return []