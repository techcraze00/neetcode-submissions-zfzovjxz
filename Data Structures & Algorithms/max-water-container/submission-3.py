class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # leftMax, rightMax = 0,0
        vol=0
        left, right = 0, len(heights)-1
        while left < right:
            h = min(heights[left], heights[right])
            area = (right-left) * h

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
            vol = max(area, vol)
        return vol

            

