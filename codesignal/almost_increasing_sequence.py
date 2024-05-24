def solution(sequence):
    count=0
    n=len(sequence)
    for i in range(n - 1):
        if sequence[i]>=sequence[i+1]:
            count+=1
            r=i
            
    if count==1:
         if isSorted(sequence[:r]+sequence[r+1:]) or isSorted(sequence[:r+1] +sequence[r+2:]) :
            return True
            
    return False
        
def isSorted(array) :

    for i in range(len(array)-1):
        if array[i]>=array[i+1]: 
            return False
    return True      
    
            
