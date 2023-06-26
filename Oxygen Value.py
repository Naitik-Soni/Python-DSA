'''
Problem Statement:
The selection of MPCS exams includes a fitness test which is conducted on the ground. There will be a batch of 3 trainees,
appearing for a running test on track for 3 rounds.

You need to record their oxygen level after every round. After trainees are finished with all rounds, calculate for each trainee 
his average oxygen level over the 3 rounds and select the one with the highest average oxygen level as the fittest trainee. 
If more than one trainee attains the same highest average level, they all need to be selected. Display the fittest trainee(or trainers) 
and the highest average oxygen level.

Example:
Input:
95
92
95
92
90
92
90
92
90

Output:
Trainee Number: 1
Trainee Number: 3
'''

trainees = []
n=9
for i in range(n):
    inp = int(input())
    if inp > 100 or inp < 0:
        print("Invalid input")
        n=n+1
    else:
        trainees.append(inp)
    
trainee1 = (trainees[0] + trainees[3] + trainees[6])/3
trainee2 = (trainees[1] + trainees[4] + trainees[7])/3
trainee3 = (trainees[2] + trainees[5] + trainees[8])/3

val = max(trainee1, trainee2, trainee3)
if trainee1 == val:
    print("Trainee number: 1")
if trainee2 == val:
    print("Trainee number: 2")
if trainee3 == val:
    print("Trainee number: 3")
