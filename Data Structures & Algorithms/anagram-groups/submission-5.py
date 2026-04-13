class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = defaultdict(list)
        for words in strs:
            sorted_char = tuple(sorted(words))
            mapped[sorted_char].append(words)
        res=[]
        for value in mapped.values():
            res.append(value)
        return res