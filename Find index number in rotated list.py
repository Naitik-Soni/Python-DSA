'''
Problem:
Find the index of given integer in the rotated list

Input:
numbers = [-1,0,42,56,89,130,169,248,-281,-218,-139,-99,-56,-23]
query = -139

Output:
10
'''

numbers = [98,87,56,43,32,23,21,10,8,4,3,0]
query = 23

def search_num(num,query):
    low, high = 0, len(num)-1
    while (high-low)>1:
        mid = (high+low)//2
        if num[mid] == query:
            return mid
        elif num[mid]>num[low]:
            if num[low]<=query and query<num[mid]:
                high=mid
            else:
                low=mid
        else:
            if num[mid]<query and query<=num[high]:
                low = mid
            else:
                high=mid
    return high if num[high]==query else low

result = search_num(numbers, query)
print(result)
