import random

weapons = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
game_won = False

def game_loop():
  while not game_won:
    player_weapon = get_weapon()
    pc_weapon = get_pc_weapon()
    victor = battle(player_weapon, pc_weapon)
    if(victor == 'player'):
      print(f'{weapons[player_weapon]} beats {weapons[pc_weapon]}. You are victorious!')
    elif(victor == 'pc'):
      print(f'{weapons[pc_weapon]} beats {weapons[player_weapon]}. You lose.')
    else:
      print('Draw! Try again...')
      game_loop()

def get_weapon():
  player_weapon = input('Choose your weapon (r, p, s): ')
  if player_weapon != 'r' and player_weapon != 'p' and player_weapon != 's':
    print(f'{player_weapon} is not a valid weapon. Please try again.')
    player_weapon = get_weapon()
  return player_weapon

def get_pc_weapon():
  return(random.choice(list(weapons)))
  
def battle(player_weapon, pc_weapon):
  if(player_weapon == pc_weapon):
    return('draw')
  elif((player_weapon == 'r' and pc_weapon != 'p') or 
       (player_weapon == 'p' and pc_weapon != 's') or 
       (player_weapon == 's' and pc_weapon != 'r')):
    return('player')
  return('pc')

game_loop()