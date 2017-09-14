# Game of Battleship
import random
import os
# Setup Variable Sets
previous_moves = set()
previous_hit = set()
grid_set = set()

# Create Grid of tuple points
def build_grid(size):
    x_axis = list(range(0, size))
    y_axis = list(range(0, size))

    for x_point in x_axis:
        for y_point in y_axis:
            grid_point = x_point, y_point
            grid_set.add(grid_point)
    return grid_set
    
# Select Difficulty
def set_difficulty():
    easy = 3
    med = 5
    hard = 15
    grid = set()
    level = ''
    while True:
        print("How difficult would you like this game to be?")
        difficulty = input("Type EASY, MED, or HARD >> ").upper()
        if difficulty == "EASY":
            grid = build_grid(easy)
            edge = easy
            count = 6
            level = 'easy'
            break
        elif difficulty == "MED":
            grid = build_grid(med)
            edge = med
            count = 20
            level = 'medium'
            break
        elif difficulty == "HARD":
            grid = build_grid(hard)
            edge = hard
            count = 40
            level = 'hard'
            break
        else:
            print("That is not a valid selection. Try again")
    return count, grid, edge, level
        

    
#Set Coordinates of Battleships  randomly 
def set_ships(grid):
# Battleship 1
    ship1coord = random.sample(grid, 1)
# Battleship 2
    ship2coord = random.sample(grid, 1)
# Battleship 3
    ship3coord = random.sample(grid, 1)
# Aggregate the ship coordinates into a set
    ship_coords_set = {ship1coord[0],ship2coord[0],ship3coord[0]}

    return ship_coords_set
    

  

# Draw the Map
def draw_grid(edge, previous_moves, previous_hits, current_move, ship_position):
    row = edge -1
    if current_move.issubset(ship_position):
        map_key = "*"
    else:
        map_key = "x"
     
    print('_.' * edge)
    while row >= 0:
        column = 0
        while column < edge:
            if (row, column) == current_move:
                if column == edge -1:
                    print('|{}|'.format(map_key))
                else:
                    print('|{}'.format(map_key), end='')
            elif (row, column) in previous_hits:
                if column == edge - 1:
                    print('|*|')
                else:
                    print('|*', end ='')
            elif (row, column) in previous_moves:
                if column == edge - 1:
                    print('|x|')
                else:
                    print('|x', end ='')
            else:
                if column == edge -1:
                    print('|_|')
                else:
                    print('|_', end='')
            column += 1
        row -=1
    return
    
# main program

# initialization
remaining, game_grid, boundary, level = set_difficulty()
ship_coords = set_ships(game_grid)
print('Welcome to Battleship! You have chosen difficulty level: {}s'.format(level))
print('\nYour battle area will be a {} x {} square'.format(boundary, boundary))
print('Enter coordinates in the format 0,0')
player_choice = input(' >>').upper()
    


# Convert input into coordinates
def convert(coord):
    try:
        tupled = tuple(map(int,coord.split(',')))[::-1]
        return tupled
    except ValueError:
        pass

# Main Loop        
while True:
    
    if player_choice == 'QUIT':
        os.system('cls' if os.name == 'nt' else 'clear') 
        break
    elif remaining < 1:
        print("You are out of torpedos! You lose! :(")
        break
    elif player_choice == 'CHEAT':
        print(ship_coords)
        player_choice = input(' >>').upper()
    elif player_choice == 'SHOW':
        print(previous_moves)
        player_choice = input(' >>').upper()
    else:
        inputted = {convert(player_choice)}
        if inputted.issubset(game_grid):
            if inputted.issubset(ship_coords):
                print("Its a hit!")
                previous_hit.update(inputted)
                previous_moves.update(inputted)
                draw_grid(boundary, previous_moves, previous_hit, inputted, ship_coords)
                print('You have {} torpedos left!'.format(remaining))
                if previous_hit == ship_coords:
                    print("You've sunk all of the enemy ships! Congratulations! You win")
                    break
                else:
                    player_choice = input(' Lets find the rest of them! >>').upper()
            else:
                print("Its a miss!")
                previous_moves.update(inputted)
                draw_grid(boundary, previous_moves, previous_hit, inputted, ship_coords)
                print('You have {} torpedos left!'.format(remaining))
                player_choice = input(' Keep Trying! >> ').upper()
        else: 
            print("Not valid! Try again!")
            print('You have {} torpedos left!'.format(remaining))
            player_choice = input(' >>').upper()
    remaining -= 1
            

