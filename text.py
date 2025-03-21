print("Welcome to my Computer Quiz")

playing = input("Do u want to play ?: ")

if playing.lower() != "yes":
    quit()
print("okay, lets play")

score = 0

answer = input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct")
    score +=1
else : 
    print("incorrect")

answer = input("what does GPU stands for? ").lower()
if answer == "graphical processing unit":
    print("correct")
    score +=1
else : 
    print("incorrect")

print("you got "+ str(score)+ " question correct")
print("you got "+ str((score/4)*100)+ " %")