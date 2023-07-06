'''
Program: Write a program to sort characters (numbers and punctuation symbols are not included) in a given string
Input:
String str = “zxcbg”

Output:
bcgxz

Explanation:
After sorting we get string as bcgxz
'''
str = input()
ls = []
for i in str:
    ls.append(ord(i))
ls.sort()
str = ""
for i in ls:
    str += chr(i)
print(str)
