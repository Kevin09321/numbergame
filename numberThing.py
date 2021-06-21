import random

number = random.randint(1,9)

chances = 1

while chances < 5 :
    guess = input("Pick A Number Between 1-9 : ")
    chances = chances + 1
    if guess == number + 1 or guess == number - 1:
        print("Your Close!")
    else: 
        print("Not Close")   
    if guess == number :
        print("You won!")
        break
    
if not chances < 5 :
    print("You Lost, the number was ", number)
