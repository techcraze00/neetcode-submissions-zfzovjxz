class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = 1,1
        n=len(nums)
        lProd = [0] * n
        rProd = [0] * n

        for i in range(n):
            j=-i-1

            lProd[i] = l
            rProd[j] = r
            l*= nums[i]
            r*= nums[j]
        
        res=[]
        for i in range(n):
            res.append(lProd[i] * rProd[i] )
        return res