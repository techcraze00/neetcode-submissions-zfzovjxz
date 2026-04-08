class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        result = 0

        while l <= r :
            mid = l + (r - l)//2

            if self.calculateHours(piles, mid) <= h:
                result = mid
                r = mid - 1
            else:
                l = mid + 1

        return result

    def calculateHours(self, piles, k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours