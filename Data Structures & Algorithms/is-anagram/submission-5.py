from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s)!=len(t)):
            return False

        '''        
        for word in set(s):
            if s.count(word) != t.count(word):
                return False
        
        return True
        '''
        return sorted(s) == sorted(t)
        
