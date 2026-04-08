class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        have = len(lookup)
        
        # window ={}
        # need = len(window)
        minLen = float('inf')
        start, end = 0,0

        result = ""

        while end < len(s):
            #end pointer
            while end < len(s) and have != 0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        have -= 1
                end+=1

            #start pointer
            while start < end and have == 0:
                if end-start < minLen:
                    minLen = end - start
                    result = s[start:end]
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]] > 0:
                        have+=1

                start +=1

        return result
