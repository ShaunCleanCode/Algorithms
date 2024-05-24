from collections import deque
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def solution(t):
    # bfs implementation
   
    traverse=[]
    queue =deque([t])
    while queue:
        v=queue.popleft()
        if v!=None:
            traverse.append(v.value)
            queue.append(v.left)
            queue.append(v.right)
        
        
    return (traverse)
        

