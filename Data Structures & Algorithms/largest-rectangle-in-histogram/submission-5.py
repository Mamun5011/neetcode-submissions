class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #initilaize stack and max_area
        stack=[]
        max_area = 0
        #Iterate through the heights array
        for i,h in enumerate(heights):
            start = i
            #continue to left shift the current height until it fits in ascending order numbers
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                max_area = max(max_area, height*(i-index))
                start=index
            #insert the current height either with original index or updated left shift index
            stack.append((start,h))

        for h in stack:
                max_area = max(max_area, h[1]*(len(heights)-h[0]))
        return max_area        