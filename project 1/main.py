import random
'''
1 for snake
0 for gun
-1 for water
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice:")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

# By now we have two numbers, you and computer

print(f"you choose: {reverseDict[you]}\ncomputer choose: {reverseDict[computer]}")

if(computer == you):
    print("It's adraw!")
else:
    if(computer == -1 and you == 1):
        print("you win!")
    elif(computer == -1 and you == 0):
        print("Ypu lose!")
    elif(computer == 1 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    else:
        print("Somthing Went Wrong!")

# if((computer - you) == -1 or (computer - you) == 2):
#     print("you lose!")
# else:
#     print("you win!")