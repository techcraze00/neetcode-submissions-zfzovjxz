class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= []

        for idx, num in enumerate(nums):

            if num > 0:
                return res
            
            if num == nums[idx-1] and idx>0:
                continue
            
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
                    while nums[left] == nums[left-1] and left < right:
                        left+=1


        return res

