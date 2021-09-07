#A progam to guess a number
# no of guesses 5
# print no of guesses left
# No of guesses he took to finish
# game over

n=15
number_of_guesses=1
print("Number of guesses limited ie 5 times")
while(number_of_guesses<=5):
    guess_number=int(input("Guess the number"))
    if guess_number<15:
        print("YOu have entred a lesser number please input a higher number.\n ")
    elif guess_number>15:
        print("You have entered a larger number please enter a lesser number ")
    else:
        print("Congratulations.\n You wone")
        print("Number of guesses you took to win,",number_of_guesses)
        break
    print(5-number_of_guesses,"Number of guesses left")
    number_of_guesses=number_of_guesses+1
if number_of_guesses>5:
    print("Game over \nBetter luck next time")