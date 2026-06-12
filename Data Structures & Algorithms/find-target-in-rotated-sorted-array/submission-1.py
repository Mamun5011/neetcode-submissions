class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # declare 2 pointer
        l = 0
        r = len(nums) - 1

        # run binary search

        while l <= r:
            # get the mid point
            mid = (l+r)//2
            # if the target is in mid point, return the index
            if nums[mid] == target:
                return mid
            # if l to mid are sorted, then check whether target is in this range or not
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # else if target falls after mid point or before l point move l after mid else move r before mid
            elif target > nums[mid] and target < nums[l]:
                l = mid + 1
            else:
                r  = mid -1
        return -1