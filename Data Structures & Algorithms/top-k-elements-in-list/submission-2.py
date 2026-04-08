class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        counter = Counter(nums)
        bucket = [0] * (n+1)
        # n+1 beacuse we account for num if occurs 0 times to n times
        # [1,2,3] --> [0,0,0,0] --> [0 times, 1 times, 2 times, all 3 times]

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        res=[]
        for i in range(n,-1,-1):
            if len(res) != k and bucket[i]!=0:
                res.extend(bucket[i])
        return res
