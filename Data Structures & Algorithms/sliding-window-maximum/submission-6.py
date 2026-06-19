class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # initialize deque
        q  = deque()
        res = []

        # iterate over the nums
        for i in range(len(nums)):
        # make sure the elements in the queue is decresing order
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

        # get rid of all previous window history if it moves to next window
            while i-q[0]+1 > k:
                q.popleft()
                
        # if current window size is greater or equal k, save current window max
            if i+1 >=k:
                res.append(nums[q[0]])
        return res

        