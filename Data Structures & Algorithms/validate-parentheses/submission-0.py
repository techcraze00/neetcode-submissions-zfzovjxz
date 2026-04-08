class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for closing in s:
            if closing in closeToOpen:
                if stack and stack[-1] == closeToOpen[closing]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(closing)
                
        return True if not stack else False