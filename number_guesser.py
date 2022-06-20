# Number Guesser - Simple beginners projects from Tech With Tim on yt
# https://youtu.be/DLn3jOsNRVE
# Generate random number and track how many times user will have to guess it

import random
# importing 'random' module of Python, that let you use all the functionality,
# that is there. There are sets of default modules, and others that you need
# to install first.

top_of_range = input("Type a number: ")
# Nom make sure, that user is entering number, and that it's greater than 0.
# Another problem is that what user will enter will come out with string ""
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    # int() function will convert a string into numeric, but when you'll enter
    # a word, it will come out as an error, so the first function here,
    # that is isdigit() will come as True if it's digit
    if top_of_range <= 0:
        print("Please type a number that is larger than 0.")
        quit()
else:
    print("Enter a number next time")
    quit()
random_number = random.randrange(0, top_of_range)
# will generate random number from top_of_range, which was provided by user
# (-5, 11) is from -5 to 10, not 11
# random.randrange(11) will start at 0, like you put only ending number
# random.randint(11) WILL INCLUDE 11
guesses = 0  # similar as on the quiz game, you set up first variable as 0, and
# then add 1 with every guess.

while True:  # while user_guess != random_number: would act the same
    guesses += 1  # every time the loop is fired you should have guesses +1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

        ''' This is less elegant way:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
        
        # elif user_guess < random_number:
        #    print("You were below the number!")
        # You don't need to check as in the comment above, because you check
        # if it's equal in the loop already. Also you don't need to check
        # it in the else statement, and indent other "if-else" if you will
        # use "elif"'''

print(f"You got it in {guesses} guesses!")
# other thing to write that string is:
# print("You got it in", guesses, "guesses.")
# You don't need to convert variable into str(), because it's int()
