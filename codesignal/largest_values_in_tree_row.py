from collections import deque
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(t):
    if t==None:
        return []
    
    queue =deque([(t,0)])
    level_max={}
    
    while queue:
        node ,level =queue.popleft()
        if level in level_max:
            level_max[level]=max(node.value,level_max[level])
        else:
            level_max[level]=node.value
            
        if node.left!=None:
            queue.append((node.left,level+1))
        if node.right !=None:
            queue.append((node.right,level+1))
            
    return [level_max[i] for i in sorted(level_max)]
            

            
         
    
    
    

    
        
    
                
        
                
    

