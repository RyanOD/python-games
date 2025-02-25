import requests

API_URL = "https://random-word-api.herokuapp.com/word"
game_won = False
alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))

def play_game():
    word = get_word() # ends game if API call fails
    word_array = ["_"] * len(word)
    guesses = ""

    while True:
        show_status(word_array, guesses)

        # end game if win conditions met
        if check_win_conditions(word, word_array):
            print("Congratulations! You win.")
            break

        # get player guess and validate
        guess = get_guess(guesses, alphabet)

        # add valid guess to guesses list
        guesses += f"{guess} "
    
        # if match, update all matching positions in word array
        if guess in word:
            word_array = find_all_positions(word, guess, word_array)
        else:
            (f"Sorry, {guess} is not in this word. Try again.")

    def get_word():
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()[0]
        else:
            print("We're sorry, no word can be selected at this time. Please try again later.")
            raise ValueError("API not responding")

def get_guess(guesses, alphabet):
    while True:
        guess = input("\nGuess a letter: ").lower()
        if guess in guesses:
            print(f"You've already guessed {guess}. Please try again.")
        elif len(guess) == 1 and guess.isalpha():
            alphabet.remove(guess)
            return guess
        else:
            print("Invalid entry. Please try again.")

def find_all_positions(word, guess, word_array):
    for index, character in enumerate(word):
        if character == guess:
            word_array[index] = guess
    return word_array

def show_status(word_array, guesses):
    print("\n")
    for character in word_array:
        print(character, end=" ")
        print("\n")
        print(f"Guesses: {guesses}")

def check_win_conditions(word, word_array):
    if word == "".join(word_array):
        return True

play_game()