class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        basket = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in basket:
                return [basket[diff], i]
            
            basket[nums[i]] = i