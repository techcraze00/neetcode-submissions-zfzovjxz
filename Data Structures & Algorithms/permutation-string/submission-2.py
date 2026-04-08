class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        
        count1 = Counter(s1)

        l=0
        r=len(s1)

        while r <= len(s2):
            count2 = Counter(s2[l:r])
            print(count2)
            if count2 == count1:
                return True
            l+=1
            r+=1
        return False
        
