from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper=defaultdict(list)

        for char in strs:
            sorted_char = tuple(sorted(char))
            mapper[sorted_char].append(char)
            
        return list(mapper.values())