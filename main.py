import random

rand = random.randint(1, 100)

while True:
    guess = int(input("Enter a number: "))
    if guess < rand:
        print("Too Low!")
    elif guess > rand:
        print("Too High!")
    else:
        print("Congratulations, the number is", guess)
        break
