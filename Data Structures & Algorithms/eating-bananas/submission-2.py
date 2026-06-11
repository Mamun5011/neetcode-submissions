class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lower bound is 1 banana and upper bound is max(nums) banana
        l = 1
        r = max(piles)
        # set initial result as highest possible banana
        res = r
        # binary search for banana count which gives us the lowest banana count
        while l <= r:
            #midpoint
            mid = (l+r)//2
            #getting the time to finish all piles
            time = sum([math.ceil(x/mid) for x in piles])
            #if the time is less than or equal threshold, update result and eliminate right portion of array
            if  time <= h:
                res = min(res, mid)
                r = mid - 1 # look for more smaller banana count next
            else:  # time needs to reduce, so increase banana count and so go beyond midpoint
                l = mid + 1
          
        
        return res