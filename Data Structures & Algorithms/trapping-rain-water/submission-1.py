class Solution:
    def trap(self, height: List[int]) -> int:
        ''' 
        #two pointer approach , Space : O(1)
        l, r = 0 , len(height)-1
        leftMax, rightMax = height[l], height[r]

        res= 0

        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        '''
        #two pointer approach, Space: O(n)
        n = len(height)
        L = [0] *n
        R = [0] *n
        leftMax = 0
        rightMax = 0
        
        for i in range(n):
            j = -i-1
            
            leftMax = max(height[i],leftMax)
            L[i] = leftMax

            rightMax = max(height[j], rightMax)
            R[j] = rightMax

        res = 0
        for i in range(n):
            if (min(L[i],R[i]) - height[i]) > 0:
                res += min(L[i],R[i]) - height[i]

        return res



