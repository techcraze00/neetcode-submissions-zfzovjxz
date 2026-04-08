class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = {}

        for num in nums:
            mapper[num] = mapper.get(num,0)+1
        
        for key, value in mapper.items():
            if value>1:
                return True
        return False
            