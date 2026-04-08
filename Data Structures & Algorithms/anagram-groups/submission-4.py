class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list) # { [a,c,t]: ["act", "cat"] }
        for word in strs:
            sorted_char = tuple(sorted(word))
            mapper[sorted_char].append(word)
        res=[]
        for value in mapper.values():
            res.append(value)
        
        return res


            

        