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

        # if the size of the window is more than k then pop
            while i-q[0]+1 > k:
                q.popleft()
                
        # append if it is in a full window
            if i+1 >=k:
                res.append(nums[q[0]])
        return res

        