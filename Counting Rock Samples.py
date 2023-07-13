'''
Problem:
Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], the task is to count the rock samples that are in 
the range ranges[i][0] to ranges[i][1], for every possible 1 <= i <= N.

Input:
samples[] = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ranges[] = [
  [300, 380],
  [400, 700]
]

Output:
2 4

Explanation: 
Range [300, 380]: Samples {345, 321} lie in the range. Therefore, the count is 2. 
Range [400, 700]: Samples {433, 604, 517, 470} lie in the range. Therefore, the count is 4.

Note: Modify samples and ranges for output.
'''

samples = [400, 567, 890, 765, 987]
ranges = [
        [300, 380], 
        [800, 1000]
]

r1 = 0
r2 = 0

for k in samples:
    if k >= ranges[0][0] and k <= ranges[0][1]:
        r1 += 1
    elif k >= ranges[1][0] and k <= ranges[1][1]:
        r2 += 1
        
print(r1, " ", r2)
