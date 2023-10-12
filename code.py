import random as rd

def operation():
    operators=["+","-","*"]
    MIN_NUM=3
    MAX_NUM=20

    operand1=rd.randint(MIN_NUM,MAX_NUM)
    operand2=rd.randint(MIN_NUM,MAX_NUM)
    operator=rd.choice(operators)

    exp=str(operand1)+operator+str(operand2)
    answer=eval(exp)
    return exp,answer

exp,answer=operation()

input("press enter to begin!")

import time
initial_time=time.time()

for i in range(0,5):
    exp,answer=operation()
    while True:
        print("problem ",i+1," ",exp,":",end='')
        guess=int(input())
        if guess==answer:
            break
final_time=time.time()
time_taken=round(final_time-initial_time,2)
print("Great Work! You finished in ",time_taken," seconds!")
