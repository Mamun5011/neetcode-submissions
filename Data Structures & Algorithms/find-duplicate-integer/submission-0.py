class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use Floyd's fast and slow pointer
        # Assume array as a linked List where each index points to next index given by its value
        slow = 0
        fast = 0
        # use slow and fast pointer; slow moves 1 step and fast moves 2 step
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
    
        # if slow and fast moves there is a loop

        # then start from the first for a new pointer and moves one step for both new and slow earlier
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        # return the slow value
        return slow