class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)
        for words in strs:
            sortedBucket = tuple(sorted(words))
            mapper[sortedBucket].append(words)
        print(mapper)

        res = []
        for value in mapper.values():
            res.append(value)
        return res