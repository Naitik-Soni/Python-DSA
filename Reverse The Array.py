'''
Problem:
Given an array of integers and position M. you have to reverse an array after that position

Input:
6 3
1 2 3 4 5 6

Output:
[1, 2, 3, 6, 5, 4]

Explaination:
Considering 0-based indexing we have M = 3 so the 
subarray[M+1 … N-1] has to be reversed.
Therefore the required output will be {1, 2, 3 , 6, 5, 4}.
'''
n = int(input())
m = int(input())
arr = []
for i in range(0,n):
    arr.append(int(input()))

for i in range(m,int((n + m)/2)):
    k = arr[i]
    arr[i] = arr[n - (i-m) - 1]
    arr[n - (i-m) - 1] = k
    
print(arr)
