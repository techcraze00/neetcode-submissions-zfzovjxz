import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        regx = r'[^a-zA-Z0-9]'
        s = re.sub(regx,"",s).lower()
        print(s)
        n=len(s)

        left = 0
        right = n-1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return False
        return True

