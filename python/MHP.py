import sys
import json
import numpy as np

data = json.loads(sys.argv[1])

NUMBER_DOORS = int(data['doors'])
NUMBER_SIMULATIONS = int(data['simulations']) 

def simulate_winnerdoors():
    return np.random.randint(0, NUMBER_DOORS, NUMBER_SIMULATIONS)

def player_guess():
    return np.random.randint(0, NUMBER_DOORS, NUMBER_SIMULATIONS)

# Creates a list without the winner doors and the guesses
def reveal_goat_door(winner_doors, guesses):
    result = [[x for x in range(NUMBER_DOORS) if x != winner_doors[i] and x != guesses[i]] for i in range(NUMBER_SIMULATIONS)]
    for i in range(NUMBER_SIMULATIONS):
        if(len(result[i]) == NUMBER_DOORS-1):
            del result[i][0]
    return result

def switch_doors(reveal_doors, guesses):
    switched_doors = [[x for x in range(NUMBER_DOORS) if x not in reveal_doors[i] and x != guesses[i]] for i in range(NUMBER_SIMULATIONS)]
    return np.reshape(switched_doors, (NUMBER_SIMULATIONS,)) 

def win_percentage(winner_doors, guesses):
    return 100 * np.mean(winner_doors==guesses)


print("Win percentage when keeping original door")
print(win_percentage(simulate_winnerdoors(), player_guess()))

winner_doors = simulate_winnerdoors()
guesses = player_guess()
reveal_goats = reveal_goat_door(winner_doors, guesses)
guesses = switch_doors(reveal_goats, guesses)

print("Win percentage when switching doors")
print(win_percentage(winner_doors, guesses))

sys.stdout.flush()