import requests

DEBUG = False

API_URL = "https://random-word-api.herokuapp.com/word"
game_won = False
guesses = []
alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))

def game_init():
  word = get_word()
  if not word:
    print("We're sorry, no word can be selected at this time. Please try again later.")
    raise ValueError("API not responding")
  else:
    word_array = ["_"] * len(word)
  
  return word, word_array

def game_loop(word, word_array):
  while not game_won:
    if DEBUG: debug(word, word_array)

    show_status(word_array)
    check_win_conditions(word, word_array)

    # get player guess and validate
    guess = get_guess(guesses, alphabet)
    
    if guess:
      # check if guess is in word
      if check_guess(guess, word):
        word_array = find_all_positions(word, guess, word_array)
      else:
        (f"Sorry, {guess} is not in this word. Try again.")

def get_word():
  response = requests.get(API_URL)
  if response.status_code == 200:
    return response.json()[0]
  else:
    return False

def get_guess(guesses, alphabet):
  guess = input("\nPlease choose a single letter or guess final word: ").lower()
  if len(guess) != 1:
    print(f"{guess} is more than one letter. Please enter a single letter.")
  elif not guess.isalpha():
    print(f"{guess} is not a valid character from the English alphabet. Please try again.")
  elif guess in guesses:
    print(f"You've already guessed {guess}. Please try again.")
  else:
    guesses.append(guess)
    alphabet.remove(guess)
    return guess
  return False

def check_guess(guess, word):
  if guess in word:
    #print(f"Good guess, {guess} is in the word!")
    return True
  else:
   # print(f"Sorry, {guess} is not in the word.")
    return False

def find_all_positions(word, guess, word_array):
  for index, character in enumerate(word):
    if character == guess:
      word_array[index] = guess
  return word_array

def show_status(word_array):
  print("\n")
  for character in word_array:
    print(character, end=" ")
  print("\n")

def check_win_conditions(word, word_array):
  if word == "".join(word_array):
    print("Congrats, you win!")
    global game_won
    game_won = True

def debug(word, word_array):
  print(f"""\n
----------------------------------------------------------------
DEBUG MODE ON
----------------------------------------------------------------
- Alphabet = {alphabet}
- Guesses = {guesses}
- Word = {word}
- Word Array = {word_array}
----------------------------------------------------------------\n""")

word, word_array = game_init()
game_loop(word, word_array)

if game_won:
  print("Congratulations! You win.")