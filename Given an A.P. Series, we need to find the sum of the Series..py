'''
Problem: Given an A.P. Series, we need to find the sum of the Series.
Input:
n=4
a=2
d=2

Output:
20

Explanation:
2+4+6+8 = 20
'''
n = int(input())
a = int(input())
d = int(input())
sum = a

for i in range(1,n):
    sum += (a + d*i)
    
print(sum)
