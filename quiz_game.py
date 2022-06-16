# Quiz Game - Simple beginners projects from Tech With Tim on yt
# https://youtu.be/DLn3jOsNRVE

print("Welcome to Quiz!")

playing = input("Do you want to play? Y/N ").lower()  # input() function allows
# user to typing in the console inside the brackets you add 'prompt' and it's
# something appears before user can start typing. Whatever they write in
# prompt, will be stored later in a variable. Adding space after prompt will
# prevent user for typing right after question mark.
variables = ["y", "yes", "tak", "t"]
if playing not in variables:
    quit()
else:
    print("Let's play!")
score = 0  # variable at the top of the program, score is equal to 0 at first

# in that case it's fine to use variable "answer" many times, since it
# was used in if-else earlier in the program
answer = input("What does CPU stand for? ").lower()
# lower() after input() allows you to check for lowercase answer match if user
# will add uppercase to the input
if answer == "central processing unit":
    print("Correct!")
    score += 1  # same as score = score + 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct!")
print(f"You got {(score/4) * 100}%.")
# I prefer f-strings over (""+str()+"")
