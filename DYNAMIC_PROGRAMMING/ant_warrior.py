# Read the total number of food stores
n = map(int,input())

# Input the amount of food stored in each food store
food_stores = map(int,input().split())

# Initialize the dynamic programming table with 100 elements
d = [0]* 100

# The first store's amount is the first entry in the dp table
d[0] = food_stores[0]
# The second entry is the maximum of the first two food stores
d[1] = max(food_stores[0], food_stores[1])

def dynamic_programming(n, food_stores, d):
    
    for i in range(2, n):
        d[i] = max(d[i-2] + food_stores[i], d[i-1])

    print(d[n-1]) 

# Execute the dynamic programming function
dynamic_programming(n, food_stores, d)
