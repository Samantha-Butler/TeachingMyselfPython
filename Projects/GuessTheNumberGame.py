import random

top_number = input("Welcome to the number guess game! First, pick the highest number you can choose up to! \n")

if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Please type a number larger than 0. Rerun to try again.")
        quit()

else: 
    print("Sorry, you will need to type a number! Rerun and try again.")
    quit()

random_number = random.randint(0, top_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("What number will you guess? \n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("I did not recognise that number, try typing a number this time.")
        continue

    if user_guess == random_number:
        print(f"CONGRATULATIONS! The secret number was {random_number}. You have guessed the number in {guesses} tries!")
        break
    elif user_guess > random_number:
        print("That number was higher than the secret number. Try again!")
    else: 
        print("That number was below the secret numer! Try again!")
