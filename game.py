from game_parser import read_lines, parse, find_player
from grid import grid_to_string

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport, Player
)
#this is just a test to see if anything is saved from here
import sys
class Game:
    def __init__(self, filename):
        self.filename = filename
        self.game_over = False
        self.move = ''
        self.player = find_player(parse((read_lines(filename))))
        self.grid = parse((read_lines(filename)))
        

    
    

    def game_move(self):
        command_move = input("Input a move: ")
        self.move = command_move.lower()
        return command_move

    def move_player(self):
        move = self.game_move()
        
        
        
        if move == "s":
            if self.check_collision(self.player.row + 1, self.player.col) == 'Air' :
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)

                self.grid[self.player.row + 1][self.player.col] = self.player
                
                self.player.row += 1

            elif self.check_collision(self.player.row+1 , self.player.col) == 'Water':
                self.player.num_water_buckets += 1
                
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row + 1][self.player.col] = self.player
                
                self.player.row += 1
                print(Water.step())
            
            
                
            elif self.check_collision(self.player.row+1, self.player.col) == "Wall":
                print(Wall.step())
            
            elif self.check_collision(self.player.row + 1, self.player.col) == "Fire":

                if self.player.num_water_buckets > 0:
                    self.player.num_water_buckets -= 1
                    
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row + 1][self.player.col] = self.player
                
                    self.player.row += 1
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_live())

                else:
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row + 1][self.player.col] = self.player
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_die())
                    exit()


                    
                    
                            


        if move == "w":
            if self.check_collision(self.player.row - 1, self.player.col) == 'Air':
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row - 1][self.player.col] = self.player
                
                self.player.row -= 1
            
            elif self.check_collision(self.player.row-1 , self.player.col) == 'Water':
                self.player.num_water_buckets += 1
                
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row - 1][self.player.col] = self.player
                
                self.player.row -= 1
                print(Water.step())
            
            elif self.check_collision(self.player.row-1, self.player.col) == "Wall":
                print(Wall.step())
            
            elif self.check_collision(self.player.row-1, self.player.col) == "Fire":

                if self.player.num_water_buckets > 0:
                    self.player.num_water_buckets -= 1
                    
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row -1 ][self.player.col] = self.player
                
                    self.player.col -= 1
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_live())

                else:
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row -1 ][self.player.col] = self.player

                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_die())
                    exit()
            
            
        
        if move == "a":
            if self.check_collision(self.player.row , self.player.col-1) == 'Air':
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row][self.player.col - 1] = self.player
                
                self.player.col -= 1
            
            elif self.check_collision(self.player.row , self.player.col-1) == 'Water':
                self.player.num_water_buckets += 1
                
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row ][self.player.col- 1] = self.player
                
                self.player.col -= 1
                print(Water.step())
            
            elif self.check_collision(self.player.row, self.player.col-1) == "Wall":
                print(Wall.step())
            
            elif self.check_collision(self.player.row, self.player.col-1) == "Fire":

                if self.player.num_water_buckets > 0:
                    self.player.num_water_buckets -= 1
                    
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row ][self.player.col- 1] = self.player
                
                    self.player.col -= 1
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_live())

                else:
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row ][self.player.col- 1] = self.player
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_die())
                    exit()
            

            
            
        
        if move == "d":
            if self.check_collision(self.player.row , self.player.col+ 1) == 'Air':
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row][self.player.col + 1] = self.player
                
                self.player.col += 1
            
            elif self.check_collision(self.player.row , self.player.col+ 1) == 'Water':
                
                self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                self.grid[self.player.row][self.player.col + 1] = self.player
                
                self.player.col += 1
                
                self.player.num_water_buckets += 1
                print(Water.step())
            
            elif self.check_collision(self.player.row, self.player.col+1) == "Wall":
                print(Wall.step())
            
            elif self.check_collision(self.player.row, self.player.col+1) == "Fire":

                if self.player.num_water_buckets > 0:
                    self.player.num_water_buckets -= 1
                    
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row ][self.player.col+ 1] = self.player
                
                    self.player.col += 1
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_live())

                else:
                    self.grid[self.player.row][self.player.col] = Air(self.player.row, self.player.col)
                
                    self.grid[self.player.row ][self.player.col+ 1] = self.player
                    
                    print(grid_to_string(self.grid, self.player))
                    print(Fire.step_die())
                    exit()
                  
        print(grid_to_string(self.grid, self.player))
            

    def check_collision(self, potential_row, potential_col):
        
        if isinstance(self.grid[potential_row][potential_col], Wall) == True:
            return 'Wall'
        elif isinstance(self.grid[potential_row][potential_col], Water) == True:
            return 'Water'
        elif isinstance(self.grid[potential_row][potential_col], Air) == True:
            return 'Air'
        elif isinstance(self.grid[potential_row] [potential_col], Fire) == True:
            return 'Fire'
        elif isinstance(self.grid[potential_row][potential_col], Teleport) == True:
            return 'Teleport'
            



        
    def run_the_game(self):
        self.move_player()
        

        return grid_to_string(self.grid, self.player)
    
    # def initial_printed_grid(self): #this retusn the grid with the player in the starting position
    #     start_position = self.get_start_position()
    #     return grid_to_string(self.grid, start_position)


    def get_next_prev_position(self):
        command_move = self.move
        self.player.pot_row = (self.player.row)
        self.player.pot_col = (self.player.col)
        #'self.player.pot_row' and 'self.player.pot_col' act as potential row and column coordinates 
        # that the player could move to, checking the cell the player is steping on 

        # this method updates the actual row and column position 
        # of the player, if a "wall" message is returned from
        #the valid_movement method, we do not update it.
        if command_move.lower() == "w":
            self.player.pot_row -= 1
            if self.valid_movement() != "wall":     
                self.player.row -= 1
            else:
                pass

        if command_move.lower() == "a":
            self.player.pot_col -=1
            if self.valid_movement() != "wall":
                self.player.col -= 1
            else:
                pass

        if command_move.lower() == "s":
            self.player.pot_row += 1
            if self.valid_movement() != "wall":
                self.player.row += 1
            else:
                pass

        if command_move.lower() == "d":
            self.player.pot_col += 1
            if self.valid_movement() != 'wall':
                self.player.col += 1
            else:
                pass
        
        #if a 'water' or 'fire' message is returned from 'valid_movement', we update the water buckets
        if self.valid_movement() == "water": 
            self.player.num_water_buckets += 1
            

        if self.valid_movement() == "survive_fire": 
            self.player.num_water_buckets -= 1

        if self.valid_movement() == "teleport": # we will replace the coordinates of the 
            i = 0
            teleport_object_1 = []              #first, we make separte empty lists for every teleport
            teleport_object_2 = []              #object there could be in a txt file.
            teleport_object_3 = []
            teleport_object_4 = []
            teleport_object_5 = []
            teleport_object_6 = []
            teleport_object_7 = []
            teleport_object_8 = []
            teleport_object_9 = []

            #now, we comb through the grid and append the row and column positions to their respective
            #empty lists.  Note there should only be two elements in each list (pair of matching teleport pads)
            while i<len(self.grid):
                a = 0
                while a<len(self.grid[i]):
                    if self.grid[i][a].display == "1":
                        teleport_object_1.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "2":
                        teleport_object_2.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "3":
                        teleport_object_3.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "4":
                        teleport_object_4.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "5":
                        teleport_object_5.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "6":
                        teleport_object_6.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "7":
                        teleport_object_7.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "8":
                        teleport_object_8.append([self.grid[i][a].row, self.grid[i][a].col])
                    elif self.grid[i][a].display == "9":
                        teleport_object_9.append([self.grid[i][a].row, self.grid[i][a].col])
                    a+= 1
                i += 1
            
            #now we determine what happens when the player either steps on a 1 or a 2 or another teleport number
            #we can use the empty lists from before; if a player's row and column positions matches those
            #values of one of the elements in the empty lists, we replace it with the other set.  Given
            #that there can only be two sets of coordinates for every teleport number, we can use index values here.
            #warning, this is really, REALLY, long, sorry in advance...

            if self.grid[self.player.row][self.player.col].display == "1":
                if  self.player.row == teleport_object_1[0][0] and self.player.col == teleport_object_1[0][1]:
                    self.player.row = teleport_object_1[1][0]
                    self.player.col = teleport_object_1[1][1]
                elif self.player.row == teleport_object_1[1][0] and self.player.col == teleport_object_1[1][1]:
                    self.player.row = teleport_object_1[0][0]
                    self.player.col =  teleport_object_1[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "2":
                if self.player.row == teleport_object_2[0][0] and self.player.col == teleport_object_2[0][1]:
                    self.player.row = teleport_object_2[1][0]
                    self.player.col = teleport_object_2[1][1]
                elif self.player.row == teleport_object_2[1][0] and self.player.col == teleport_object_2[1][1]:
                    self.player.row = teleport_object_2[0][0]
                    self.player.col =  teleport_object_2[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "3":
                if self.player.row == teleport_object_3[0][0] and self.player.col == teleport_object_3[0][1]:
                    self.player.row = teleport_object_3[1][0]
                    self.player.col = teleport_object_3[1][1]
                elif self.player.row == teleport_object_3[1][0] and self.player.col == teleport_object_3[1][1]:
                    self.player.row = teleport_object_3[0][0]
                    self.player.col =  teleport_object_3[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "4":
                if self.player.row == teleport_object_4[0][0] and self.player.col == teleport_object_4[0][1]:
                    self.player.row = teleport_object_4[1][0]
                    self.player.col = teleport_object_4[1][1]
                elif self.player.row == teleport_object_4[1][0] and self.player.col == teleport_object_4[1][1]:
                    self.player.row = teleport_object_4[0][0]
                    self.player.col =  teleport_object_4[0][1]

            if self.grid[self.player.row][self.player.col].display == "5":
                if self.player.row == teleport_object_5[0][0] and self.player.col == teleport_object_5[0][1]:
                    self.player.row = teleport_object_5[1][0]
                    self.player.col = teleport_object_5[1][1]
                elif self.player.row == teleport_object_5[1][0] and self.player.col == teleport_object_5[1][1]:
                    self.player.row = teleport_object_5[0][0]
                    self.player.col =  teleport_object_5[0][1]

            if self.grid[self.player.row][self.player.col].display == "6":
                if self.player.row == teleport_object_6[0][0] and self.player.col == teleport_object_6[0][1]:
                    self.player.row = teleport_object_6[1][0]
                    self.player.col = teleport_object_6[1][1]
                elif self.player.row == teleport_object_6[1][0] and self.player.col == teleport_object_6[1][1]:
                    self.player.row = teleport_object_6[0][0]
                    self.player.col =  teleport_object_6[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "7":
                if self.player.row == teleport_object_7[0][0] and self.player.col == teleport_object_7[0][1]:
                    self.player.row = teleport_object_7[1][0]
                    self.player.col = teleport_object_7[1][1]
                elif self.player.row == teleport_object_7[1][0] and self.player.col == teleport_object_7[1][1]:
                    self.player.row = teleport_object_7[0][0]
                    self.player.col =  teleport_object_7[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "8":
                if self.player.row == teleport_object_8[0][0] and self.player.col == teleport_object_8[0][1]:
                    self.player.row = teleport_object_8[1][0]
                    self.player.col = teleport_object_8[1][1]
                elif self.player.row == teleport_object_8[1][0] and self.player.col == teleport_object_8[1][1]:
                    self.player.row = teleport_object_8[0][0]
                    self.player.col =  teleport_object_8[0][1]
            
            if self.grid[self.player.row][self.player.col].display == "9":
                if self.player.row == teleport_object_9[0][0] and self.player.col == teleport_object_9[0][1]:
                    self.player.row = teleport_object_9[1][0]
                    self.player.col = teleport_object_9[1][1]
                elif self.player.row == teleport_object_9[1][0] and self.player.col == teleport_object_9[1][1]:
                    self.player.row = teleport_object_9[0][0]
                    self.player.col =  teleport_object_9[0][1]
            

        if command_move == "q":
            exit('\nBye!')
        if command_move == "e":
            pass
        
        #after we're done altering the row and column positions, we then return them in a player class.
        new_row_pos = self.player.row
        new_col_pos = self.player.col
        return Player(self.player.num_water_buckets, new_row_pos, new_col_pos)                

    def valid_movement(self): # this instance method checks for the type of cell the proposed row 
                            # and col position that it is moving to (wall, water, fire, teleport), and then it returns 
                            # a message that is passed to the instance method named current_printed_grid
        self.grid = parse(read_lines(self.filename))
        teleport_element = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        a = 0
        while a<len(self.grid):
            j = 0
            while j<len(self.grid[a]):
                if self.grid[a][j].display == "*" and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col or self.player.pot_row < 0 or \
                self.player.pot_col <0 or self.player.pot_row > len(self.grid)-1 or self.player.pot_col > len(self.grid[a])-1:
                    return "wall"
                
                #this method checks if the player is running into a wall, or trying to exit the grid via
                #the entrance point or hole in the perimeter

                elif self.grid[a][j].display == "W" and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col:
                    return "water"
                #this method checks if the player steps on a water cell

                elif self.grid[a][j].display == " " and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col:
                    return "air"
    
                elif self.grid[a][j].display == "F" and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col:
                    if self.player.num_water_buckets >= 0:
                        return "survive_fire"
                    elif self.player.num_water_buckets < 0:
                        return "defeat"
                
                elif self.grid[a][j].display in teleport_element and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col:
                    return "teleport"
                
                elif self.grid[a][j].display == "Y" and self.player.pot_row == self.grid[a][j].row \
                and self.player.pot_col == self.grid[a][j].col:
                    return "victory"
                

                j += 1
            a += 1

    def current_printed_grid(self): # this instance method will return an updated grid, depending on the return result of valid_movement()
        player_position = self.get_next_prev_position() 
        # new_grid = self.grid
        message = ""
        # while True:
        if self.valid_movement() == 'wall':
            message +='\n'+ Wall.step() + '\n'

        if self.valid_movement() == "water": #this method was supposed to replace a given water cell
            water_row = self.player.row      # with an air cell, which it does, but for some reason, the grid
            water_col = self.player.col      # reverts back to its original state.
            self.grid[water_row][water_col] = Air(water_row, water_row)
            message += Water.step() +'\n'
        
        elif self.valid_movement() == "defeat": #this returns the message if the player dies
            message += Fire.step_die() + '\n'

        elif self.valid_movement() == "survive_fire": #this returns the message if the player lives
            message += Fire.step_live() + '\n'
        
        elif self.valid_movement() == "teleport": #this returns the message if the player steps on a water cell
            message += '\n' +Teleport.step() + '\n'

        return message