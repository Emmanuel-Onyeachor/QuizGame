print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay, let's play! :) ")
score = 0

answer = input("what does CPU stand for? ")
if answer.lower() == "Central Processing Unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does GPU stand for? ")
if answer.lower() == "Graphics Processing Unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does RAM stand for? ")
if answer.lower() == "Random Access Memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("what does PSU stand for? ")
if answer.lower() == "Power Supply":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%!")