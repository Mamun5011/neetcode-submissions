"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        #initilaize a hash table which will contain the copied list corresponding to original list
        old_to_new = {None:None}

        # create only the copy of the node without linkage
        cur = head

        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next

        # Copy the linkage in the earlier copied node
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next
        return old_to_new[head]