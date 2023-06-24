'''
Problem: Given the marks of N students in an Array A, calculate the mean
Input:
N = 4 
A = { 56 , 67 , 30 , 79 }

Output:
58

Explanation:
56+67+30+79 = 232;  232/4 = 58.
So, the Output is 58.
'''
class Solution:
    def mean(self, N , A):
        sum = 0
        for i in A:
            sum += i
        
        return int(sum/N)

obj = Solution()
N = int(input())
A = []
for k in range(N):
    A.append(int(input()))

print(obj.mean(N,A))
