'''
Program:
Given a number, the task is to check if it is tidy or not. A tidy number is a number whose digits are in non-decreasing order.

Input:
1234

Output:
Yes

Input:
1243

Output:
No

Explanation:
Digits “4” and “3” violate the property.
'''
n = int(input())
a = n
tidy = 1

while a>0:
    k = a%10
    a = a//10
    s = a%10
    if s<=k:
        tidy = 1
    else:
        tidy = 0
        break
    
if tidy == 1:
    print("Number is Tidy")
else:
    print("Number is not Tidy")
