import random
LOWER = 0
UPPER = 100
NUMBER = random.randint(LOWER, UPPER)

# game loop runs until game_won is True
def game_loop():
    game_won = False

    while not game_won:
        guess = get_guess()
        result = check_guess(guess, NUMBER)
        if result == "correct":
            print("Congrats! You win.")
            game_won = True
        else:
            print(f"Your guess is {result}. Try again...")

# get user guess and return to game_loop
def get_guess():
    return(int(input("Enter guess: ")))

# evaluate user guess versus random value and return result to game_loop
def check_guess(guess, NUMBER):
    if(guess < NUMBER):
        return("too low")
    elif(guess > NUMBER):
        return("too high")
    return("correct")

# start game_loop
game_loop()