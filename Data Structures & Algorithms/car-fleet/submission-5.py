class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #load pos and speed in a stack
        poswithSpeed = [[x,y] for x,y in zip(position,speed)]
        poswithSpeed.sort()
        stack=[(target-x)/y*1.0 for x,y in poswithSpeed]

        size = len(position)

        cur_time = stack.pop()
        res = 1
        # iterate the stack 
        while stack:
            prev_time = stack.pop()
            if prev_time <= cur_time:
                continue
    
            res+=1
            cur_time = prev_time
          
        return res




        
        res = []
        for pos,sp in zip(position,speed):
            res.append(math.ceil((target - pos)/sp))
        
        print(res)
        res = set(res)

        return len(res)
        