# Previous apply insertion sort 

array=[7,5,9,3,3,5,1,3,5,8,1,0]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]< array[j-1]:
            array[j-1],array[j]=array[j],array[j-1]
        else: 
            break


print(array)
