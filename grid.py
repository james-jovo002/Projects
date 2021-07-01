from game_parser import (read_lines, parse)
from cells import (Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport)
def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    i = 0
    printed_grid ="" #We will use nested loops to keep adding each element of the list of list of cells to this empty string
    while i<len(grid):
        a = 0
        while a<len(grid[i]):
            printed_grid += grid[i][a].display
            a += 1
        i += 1            
        printed_grid += '\n' #After we are done converting each element of the list of list of cells, we move to the next list of list of cells
    

    
    if player.num_water_buckets==0 or player.num_water_buckets>1:
        return printed_grid + '\n' + "You have {} water buckets.".format(player.num_water_buckets) + '\n'
    if player.num_water_buckets == 1:
        return printed_grid + '\n' + "You have 1 water bucket." + '\n'
    if player.num_water_buckets <0:
        return printed_grid + '\n' + "You have 0 water buckets." + '\n'
    
    return printed_grid.strip()