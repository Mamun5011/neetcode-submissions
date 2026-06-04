class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        val=1
        for i in range(len(nums)):
            left.append(val)
            val*=nums[i]
        right = [0 for i in range(len(nums))]
        val = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = val
            val*=nums[i]
        res=[]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res