class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # only add open paranthesis if open < n
        # only add closing paranthesis if closed < open
        # stop adding if open == closed == n i.e. it is valid

        stack = []
        result = []

        def backtrack (openP, closedP ):
            if openP == closedP == n:
                result.append("".join(stack))
                return 
            if openP < n:
                stack.append("(")
                backtrack(openP+1, closedP)
                print("open",stack)
                stack.pop()
            if closedP < openP:
                stack.append(")")
                backtrack(openP, closedP+1)
                stack.pop()

        backtrack(0,0)
        return result

                
                        
