class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r)//2
            if mid - 1 >=0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[l] <= nums[r]:
                return nums[l] 
            elif nums[l] <=nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        

        