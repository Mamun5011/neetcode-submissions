class Solution:
    def findMin(self, nums: List[int]) -> int:

        # fix 2 pointer from beginning and end
        l = 0
        r = len(nums) - 1
        # run binary search
        while l <= r:
            mid = (l+r)//2
            # if there is a break of ascending order, then we got the minimum
            if mid - 1 >=0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            # if the numbers are sorted from begining to end, then the first one is minimum
            elif nums[l] <= nums[r]:
                return nums[l] 
            # if numbers from left pointer to mid point are sorted, then look for the breaking point from mid to r pointer
            elif nums[l] <=nums[mid]:
                l = mid + 1
            # look for the breaking point within left point to mid point.
            else:
                r = mid - 1
        

        