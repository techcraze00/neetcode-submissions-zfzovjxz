class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
        # print(row[-1])  
            if row[-1] >= target: 
                print(row)
                left, right = 0, len(row)-1

                while left<=right:
                    mid = left + ((right-left)//2)

                    if row[mid] == target:
                        return True

                    elif row[mid] < target:
                        left = mid+1
                    
                    elif row[mid] > target:
                        right = mid-1
        return False