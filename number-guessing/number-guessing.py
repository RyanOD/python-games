import random
lower = 0
upper = 100

number = random.randint(lower, upper)

def game_loop():
  game_won = False

  while not game_won:
    guess = get_guess()
    result = check_guess(guess, number)
    if result == 'correct':
      print('Congrats! You win.')
      game_won = True
    else:
      print(f'Your guess is {result}. Try again...')
  
def get_guess():
  return(int(input("Enter guess: ")))

def check_guess(guess, number):
  if(guess < number):
    return("too low")
  elif(guess > number):
    return("too high")
  return('correct')

game_loop()