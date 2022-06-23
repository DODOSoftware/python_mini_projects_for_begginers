# Number Guesser - Simple beginners projects from Tech With Tim on yt
# https://youtu.be/DLn3jOsNRVE

# Basic structure and nesting for choose your adventure text game/book. I got
# the idea - you're nesting one if into the another, on and on to complete the
# game. Kind of fun, but I don't have the time right now to write more ifs.
# Someday maybe ;)

name = input("Choose your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You woke up on the dirt road inside the forest. Your head "
               "hurts as hell pounding inside your skull, and you have no idea "
               "how you ended here. Which way you want to go? Left (1) or "
               "right (2) ")
if answer == "1":
    answer = input("After 10 minutes of dizzy walk, you stumble upon a "
                   "fast-flowing broad river - try to swim it (1) or "
                   "go along the riverside (2)?: ")
    if answer == "1":
        print("You where to tired, started to swallow dirty water, and "
              "after short while you've drowned, never to be found... "
              "Game over.")
        quit()
    elif answer == "2":
        print("You were walking for miles, eventually tried to drink "
              "water directly form the river. After a few hours it made "
              "you sick. The water was dirty and made your stomach ache. "
              "You would swore you felt your bowels to twist inside, "
              "leaving you without strength. This was slow, painful and "
              "long death. Game over.")
        quit()
    else:
        print("Not a valid option.")
        quit()
elif answer == "2":
    answer = input("After a few miles you came to the bridge on the tiny "
                   "river. Do you want to cross the bridge (1) or turn "
                   "back (2)? ")
    if answer == "1":
        answer = input("You crossed the bridge and walk another few miles to "
                       "find a hut inside the forest, beside your dirt road. "
                       "Check if someone is there (1), or go down the "
                       "road(2)? ")
        if answer == "1":
            print("You found a kind man, who offered to help you. "
                  "You won the game!")
            quit()
        elif answer == "2":
            print("After few miles you were abducted by little green aliens, "
                  "who took abducted you and made painful experiments on you. "
                  "Always try to find help if you were lost in the forest XD "
                  "Game over.")
            quit()
        else:
            print("Not a valid option.")
            quit()
else:
    print("Choose where are you going (1 or 2). Game ended.")

print(f"Great gaming, thank you {name} :)")
