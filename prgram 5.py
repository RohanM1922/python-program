import random
import time

OPERATOR =['+','-','*']
MIN_NUM = 3
MAX_NUM = 18
TOTAL_PROBLEMS = 10

def problem():
    left = random.randint(MIN_NUM,MAX_NUM)
    operator = random.choice(OPERATOR)
    right = random.randint(MIN_NUM,MAX_NUM)

    expr = str(left) +" "+ operator+" "+str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0

input("press enter to start!")
print("-----------------")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = problem()
    while True:
        guess = input('Problem#'+ str(i+1)+ ": "+ expr + "=")
        if guess == str(answer):
            break
        wrong +=1
        if wrong == 5:
            print("attempts exceeded")
            quit()
    
end_time = time.time()
total_time = round(end_time- start_time,2)
print("-----------")
print("good work,you took", str(total_time),"sec")




