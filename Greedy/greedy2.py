

def find_big_number(array):
    n= len(array)
    result=0
    for i in range(0,n-1):
        if (array[i]!=0 and array[i+1]!=0 and result!=0):
            result *=array[i+1]
            print(f"mult{result}")
        elif (array[i]!=0 and array[i+1]!=0 and result==0):
            result =array[i]*array[i+1]
            print(f"mult{result}")
        else:
            result +=array[i+1]
            print(f"plus{result}")
    return result
44
def main():
    
    array = list(map(int, input()))
    result =find_big_number(array)
    print(result)
    
            
main()
        
