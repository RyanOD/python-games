import requests

API_URL = "https://random-word-api.herokuapp.com/word"

def game_loop():
  word = get_word()
  word_dict = string_to_dict(word)
  print(word_dict)
  guess = get_guess()
  if(check_guess(guess)):


def get_word():
  response = requests.get(API_URL)
  if(response.status_code == 200):
    return response.json()
  else:
    print("We're sorry, no word can be selected at this time. Please try again later.")

def string_to_dict(word):
  dict = {}
  for char in word[0]:
    dict[char] = 0
  return dict

def get_guess():
  guess = input("Please choose a single letter: ")
  if(len(guess) != 1 or not guess.isalpha()):
    print(f"{guess} is an invalid character. Please try again.")
    get_guess()
  return guess

def check_guess(guess, dict):
  if(guess in dict.values):
    return True
  return False

game_loop()