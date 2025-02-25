# generate secret number
import random

# welcome player to Bulls and Cows
def game_play():
    secret = generate_secret()
    print(secret)
    attempts = 0

    print("Welcome to Bulls and Cows!")
    print("All guesses must be four integer values between 0 and 9 with no repeated values.")
    print("--")

    while True:
        # set bulls and cows to zero each round
        bulls = 0
        cows = 0

        # prompt player for guess
        guess = int(input("Enter your guess: "))

        # validate guess
        if(guess > 1000 and guess < 10000 and validate_guess(guess)):
            bulls, cows = calc_bulls_cows(secret, guess, bulls, cows)
        else:
            print("Invalid guess. Please try again.")

        # show round results
        print(f"{bulls} bulls, {cows} cows")

        if bulls == 4:
            print("You win!")
            break

def generate_secret():
    secret = 10000
    while not validate_guess(secret):
        secret = random.randint(999, 10000)
    return secret
  
def validate_guess(num):
    if len(set(str(num))) != len(str(num)):
        return False
    return True

def calc_bulls_cows(secret, guess, bulls, cows):
    for i in range(0, 3):
        if str(guess)[i] in str(secret):
            if str(guess)[i] == str(secret)[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

game_play()