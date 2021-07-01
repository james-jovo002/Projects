from game import Game
from game_parser import read_lines, parse
import os
import sys
# Your code...
if len(sys.argv) == 1:
    print("Usage: python3 run.py <filename> [play]")
    exit()

filename = sys.argv[1]
number_of_moves = 0
game_over = False
list_of_inputs = ""

game = Game(filename)

# print(game.initial_printed_grid())


valid_inputs = ["w", "a", "q", "e", "s", "d"]
i = 0
while game.game_over == False:
    game.move_player()

    


    # if game.game_move().lower() in valid_inputs: 
    #     print(game.current_printed_grid())      #this prints current grid and player values
    #     if game.valid_movement()!= "wall":
    #         number_of_moves += 1 #increment the number of moves
    #         list_of_inputs += game.list_of_moves[i].lower() + ', '

    # else:
    #     print(game.current_printed_grid())
    #     print("Please enter a valid move (w, a, s, d, e, q).")
    #     print("")
    #  #concatenate the inputs made.
    # i += 1
    

    # if game.valid_movement() == "victory":
    #     print("")
    #     print("You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
    #     print("")
    #     if number_of_moves != 1:
    #         print("You made {} moves.".format(number_of_moves))
    #         print("Your moves: {}".format(list_of_inputs.strip(', ')))
    #     else:
    #         print("You made {} move.".format(number_of_moves))
    #         print("Your move: {}".format(list_of_inputs.strip(', ')))
    #     print("")
    #     print("=====================" + '\n' +\
    #         "====== YOU WIN! =====" + '\n' +\
    #         "=====================")
    #     break

    # if game.valid_movement() == "defeat":
    #     print("The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.")
    #     print("")
    #     print("You made {} moves.".format(number_of_moves))
    #     print("Your moves: {}".format(list_of_inputs.strip(', ')))
    #     print("")
    #     print("=====================" + '\n' +\
    #         "===== GAME OVER =====" + '\n' +\
    #         "=====================")
    #     break
    