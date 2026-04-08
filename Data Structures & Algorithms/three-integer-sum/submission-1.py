class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []

        # get the first item for the three integers
        for idx, num in enumerate(nums):

            #if first num in sorted arr is +ve then the sum cannot be 0
            if num > 0:
                return res
            
            #ignore the num if the curr and prev are same
            if num == nums[idx-1] and idx>0:
                continue
            
            # logic for 2 sum in sorted arr
            left, right = idx+1, len(nums)-1

            while left < right:
                Sum = num+ nums[left] + nums[right]

                if Sum>0:
                    right-=1
                elif Sum<0:
                    left+=1
                else:
                    res.append([num, nums[left], nums[right]])
                    left+=1
                    
                    #logic to skip the curr and prev number if same
                    while nums[left] == nums[left-1] and left < right:
                        left+=1


        return res

