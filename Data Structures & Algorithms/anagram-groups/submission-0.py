from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper=defaultdict(list)

        for char in strs:
            sorted_char = tuple(sorted(char))
            mapper[sorted_char].append(char)
        # print(mapper)

        # for value in mapper.values():
        #     return value
        
        return list(mapper.values())