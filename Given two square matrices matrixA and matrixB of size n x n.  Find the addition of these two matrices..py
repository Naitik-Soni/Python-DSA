'''
Problem: Given two square matrices matrixA and matrixB of size n x n.  Find the addition of these two matrices.

Input: matrixA = {{1, 2}, {3, 4}},
       matrixB = {{4, 3}, {2, 1}}
       
Output: {{5, 5}, {5, 5}}
'''

class Solution:
    def Addition(self, matrixA, matrixB):
	    rows = len(matrixA)
	    newMatrix = []
	    for i in range(rows):
		    summation = []
		    for j in range(rows):
		        summation.append(matrixA[i][j] + matrixB[i][j])
		        
		    newMatrix.append(summation)
	    return newMatrix
	    
obj = Solution()
n = int(input())
matA = []
matB = []
for i in range(n):
    ls = []
    for j in range(n):
        ls.append(int(input()))
    matA.append(ls)

for i in range(n):
    ls = []
    for j in range(n):
        ls.append(int(input()))
    matB.append(ls)
        

print(obj.Addition(matA, matB))
