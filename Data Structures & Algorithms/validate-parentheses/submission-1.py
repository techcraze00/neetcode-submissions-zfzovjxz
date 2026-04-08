class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. closed <= open 
        2. open <= n
        3. end when close = open = n

        '''

        closeToOpen = { ")" : "(", 
                        "]" : "[",
                        "}" : "{" }
        stack=[]

        for opening in s:
            if opening in closeToOpen:
                if stack and stack[-1] == closeToOpen[opening]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(opening)

        return True if not stack else False