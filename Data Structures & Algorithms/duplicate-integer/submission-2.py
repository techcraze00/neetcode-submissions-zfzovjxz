class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        basket = set()
        for i in nums:
            if i not in basket:
                basket.add(i)
                continue
            return True
        return False