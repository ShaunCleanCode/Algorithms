
array=[1,7,9,33,1,4,2,0,12,4,7]



def quick_sort(array,start,end):
    if start >=end:  # 원소가 1개인 경우 종료 
        return 
    
    pivot =start     # 피봇은 첫번째 원소
    left =start +1
    right =end
    while (left <=right) :
        # 왼쪽부터 피봇보다 큰 값을 찾을 떄 까지 반복
        while (left <=end and array[pivot] >=array[left]):
            left +=1
        # 오른쪽부터 피봇보다 작은 값을 찾을 떄 까지 반복
        while (right >start and array[pivot] <=array[right]):
            right -=1
        # 엇갈렸다면 작은값과 피봇값을 스왑
        if right <left :
            array[right],array[pivot] =array[pivot],array[right]
        # 엇갈리지 않았다면 찾은 작은 값과 큰 값을 스왑
        else:
            array[left],array[right] =array[right],array[left]
        
    quick_sort(array,start,right -1)
    quick_sort(array,right +1,end)
        


quick_sort(array,0,len(array)-1)
print(array)
        
            