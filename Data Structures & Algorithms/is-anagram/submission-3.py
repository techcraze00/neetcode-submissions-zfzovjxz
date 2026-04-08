from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapper_s={}
        mapper_t = {}

        if len(s) != len(t):
            return False

        for letter_s in s:
            mapper_s[letter_s] = mapper_s.get(letter_s,0)+1
        
        # print(mapper.items())
        for letter_t in t:
            mapper_t[letter_t] = mapper_t.get(letter_t,0)+1

        return mapper_s == mapper_t


        
