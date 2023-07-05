'''
Problem: Check if the number is a Harshad(or Niven) number or not
Input:
378

Output:
Yes it is a Harshad number

Explanation:
3+7+8=18. 378 is divisible by 18. Therefore 378 is a harshad number
'''
n = int(input())
a = n
sum = 0

while a>0:
    sum += a%10
    a //=10
a
if n%sum == 0:
    print("Yes it is a Harshad number")
else:
    print("It is not a Harshad number")
