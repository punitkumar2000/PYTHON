#Total no of guesses is 9
#Print no of guesses left
#No of guesses he took to finish
#Game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :"))
    if guess_number < 18:
        print("You had entered Lesser number please enter the Greater number.\n")
    elif guess_number > 18:
        print("You had entered Greater number please enter the Lesser number.\n ")
    else:
        print("You Won\n")
        print("No. of guesses you took to finish:", number_of_guesses)
        break
    print("No. of guesses left:", 9 - number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

