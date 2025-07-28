

# Sorting Hat

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer1 = int(input("Q1: Do you like Dusk or Dawn? (1 = Dawn, 2 = Dusk): "))
# answer_1 = Enter your answer (1-2)

if answer1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong input.")

answer2 = int(input(
    "Q2: When I am dead, I want people to remember me as? (1 = The Good, 2 = The Great, 3 = The Wise, 4 = The Bold): "))

if answer2 == 1:
    hufflepuff += 2

elif answer2 == 2:
    slytherin += 2

elif answer2 == 3:
    ravenclaw += 2

elif answer2 == 4:
    gryffindor += 2

else:
    print("Wrong input.")


answer3 = int(input(
    "Q3:  Which kind of instrument most pleases your ear (1 = The violin, 2 = The trumpet, 3 = The piano, 4 = The drum): "))


if answer3 == 1:
    slytherin += 4

elif answer3 == 2:
    hufflepuff += 4

elif answer3 == 3:
    ravenclaw += 4

elif answer3 == 4:
    gryffindor += 4

else:
    print("Wrong input.")


# Find the highest score
if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("🦁 Gryffindor")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("🦅 Ravenclaw")
elif hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
    print("🦡 Hufflepuff")
else:
    print("🐍 Slytherin")

# End of Sorting Hat code
