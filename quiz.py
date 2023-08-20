print("Welcome to my computer quiz!\n")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play :) \n")

score = 0

answer = input('Which planet is known as the "Red Planet"?\n')

if answer.lower() == "mars":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input('Who painted the Mona Lisa?\n')

if answer.lower() == "leonardo da vinci":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input('What is the capital city of Australia?\n')

if answer.lower() == "canberra":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input('What is the largest ocean on Earth?\n')

if answer.lower() == "pacific ocean" or answer.lower() == "pacific":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")


answer = input('How many colors are there in a rainbow?\n')

if answer == "7" or answer.lower() == "seven":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/5 *100) + "%")