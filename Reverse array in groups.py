'''
Problem:
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}

Output:
3 2 1 5 4
'''
def reverseInGroups(arr, N, K):
    m = N//K
    for i in range(m):
        x = K*i
        for j in range(int(K/2)):
            arr[x + j], arr[x + K - j - 1] = arr[x + K - j - 1], arr[x + j]
    
    s = N%K
    for i in range(int(s/2)):
        arr[m*K + i], arr[N - 1 - i] = arr[N - 1 - i], arr[m*K + i]
    
arr = [5,8,1,3,9,10,21,6,2,11,18]
reverseInGroups(arr, 11, 5)
print(arr)
