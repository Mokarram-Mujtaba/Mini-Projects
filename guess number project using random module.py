import random
randomNumber=random.randint(1,100)
user_guess=None
guess=0
while(user_guess!=randomNumber):
    user_guess=int(input("Guess the Number"))
    guess +=1
    if(user_guess == randomNumber):
        print("Your Guess is right")
    else:
        if(user_guess>randomNumber):
            print(("You guessed it wrong please enter a smaller number"))
        else:
            print("You guessed it wrong please enter a larger number")
print(f"you guess the number in {guess} guesses")

# print(randomNumber)
with open("highscore.txt", "r") as f:
    highscore = int(f.read())

if(guess<highscore):
    print("You have just broken the high score!")
    with open("highscore.txt", "w") as f:
        f.write(str(guess))