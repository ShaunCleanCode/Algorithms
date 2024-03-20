# Previous apply selection sort 

array=[7,5,9,3,3,5,1,3,5,8,1,0]

for i in range(len(array)):
    min_index =i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index =j
    array[i],array[min_index]= array[min_index],array[i]
    

print(array)
