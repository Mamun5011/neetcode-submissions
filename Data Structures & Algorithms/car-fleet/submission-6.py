class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort based on position for (pos, speed) pairs
        poswithSpeed = [[pos,sp] for pos,sp in zip(position,speed)]
        poswithSpeed.sort()
        
        #insert time required to reach to destination within a stack
        stack=[(target-pos)/sp*1.0 for pos,sp in poswithSpeed]

        size = len(position)
        # get the last Car fleet time to reach destination
        cur_time = stack.pop()
        res = 1
        # iterate the stack 
        while stack:
            prev_time = stack.pop()
            # if prev_car required time is equal or less it will be part of this fleet
            if prev_time <= cur_time:
                continue
    
            res+=1
            cur_time = prev_time
          
        return res
        