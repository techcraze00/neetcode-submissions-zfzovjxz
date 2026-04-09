class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        
        # i=0
        # j=1

        # while j<len(stones):
        #     if stone[j] - stone[i] == 0:
        #         i+=2
        #     i += 1
        #     j = i+1
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur:
                stones.append(cur)

        return stones[0] if stones else 0