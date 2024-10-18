print("Welcome to the Animal Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's get started!")
score = 0

# Question 1
answer = input("Which animal is known as the King of the Jungle? ")
if answer.lower() == "lion":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Lion'.")

# Question 2
answer = input("Which bird is known for its ability to mimic sounds, including human speech? ")
if answer.lower() == "parrot":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Parrot'.")

# Question 3
answer = input("What is the largest mammal in the world? ")
if answer.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Blue whale'.")

# Question 4
answer = input("Which animal is known for its long neck and spots? ")
if answer.lower() == "giraffe":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Giraffe'.")

# Question 5
answer = input("Which animal is famous for having a pouch to carry its babies? ")
if answer.lower() == "kangaroo":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Kangaroo'.")

# Question 6
answer = input("Which animal is known for changing its color to blend with its surroundings? ")
if answer.lower() == "chameleon":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Chameleon'.")

# Question 7
answer = input("Which animal has black and white stripes? ")
if answer.lower() == "zebra":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Zebra'.")

# Question 8
answer = input("Which animal can fly but is not a bird? ")
if answer.lower() == "bat":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Bat'.")

# Question 9
answer = input("What is the fastest land animal? ")
if answer.lower() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Cheetah'.")

# Question 10
answer = input("Which bird is known for being flightless and is the largest bird in the world? ")
if answer.lower() == "ostrich":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Ostrich'.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%. ")
