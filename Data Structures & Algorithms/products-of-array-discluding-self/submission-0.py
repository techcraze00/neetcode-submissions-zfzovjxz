class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        
        L=[0]*n
        R=[0]*n
        l=1
        r=1

        for i in range(n):
            j = -i-1

            L[i] = l
            R[j] = r
            l *= nums[i]
            r *= nums[j]

        for i in range(n):
            nums[i] = L[i] * R[i]



        return nums