class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #check whether both list are empty
        if not nums1 and not nums2:
            return None
    # Make the first list small to make complexity O (log(m)) where m is the length of minimum array
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m = len(nums1)
        n = len(nums2)

  
        half = (m+n)//2

        l = 0
        r = m   # could take m -1, then we had to put extra check if nums1 is empty give median from nums2
    
    #run binary search to the small list
        while l <= r:
            i = (l+r)//2 # will take total i elements from nums1
            j = half - i # will take j elements from nums2

    # split the small array into 2 part
            nums1_l = nums1[i-1] if i > 0 else float('-inf')
            nums1_r = nums1[i] if i < m else float('inf')

    # split the large array into 2 part
            nums2_l = nums2[j-1] if j > 0 else float('-inf')  
            nums2_r = nums2[j] if j < n else float('inf')


    # compare left part with right part for both array
    # if left parts are sorted w r t right part ( for both array), calculate median

            if nums1_l <=nums2_r and nums2_l <= nums1_r:
                if (m+n)%2:
                    return min(nums1_r,nums2_r)
                else:
                    return (max(nums1_l,nums2_l)+min(nums1_r,nums2_r))/2

            elif nums1_l > nums2_r:
                r = i - 1
            else:
                l = i + 1

        # update l or r if splited parts are not sorted

        