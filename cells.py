class Start:
    def __init__(self, row, col):
        self.display = 'X'
        self.row = row
        self.col = col

    def step(self, game):
        pass

class Player:
    def __init__(self, num_water_buckets, row, col):
        self.display = 'A'
        self.num_water_buckets = num_water_buckets
        self.row = row
        self.col = col
        self.pot_row = row
        self.pot_col = col

class End:
    def __init__(self, row, col):
        self.display = 'Y'
        self.row = row
        self.col = col

    def step(self, game):
        return "You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands."
        


class Air:
    def __init__(self, row, col):
        self.display = ' '
        self.row = row
        self.col = col
    def step(self, game):
        pass


class Wall:
    def __init__(self, row, col):
        self.display = '*'
        self.row = row
        self.col = col

    def step():
        return "You walked into a wall. Oof!\n"


class Fire:
    def __init__(self, row, col):
        self.display = 'F'
        self.row = row
        self.col = col
    
    def step_live():
        return '\n'+'With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!\n'
    
    def step_die():
        return '\n' + '\n'+'You step into the fires and watch your dreams disappear :(.\n'

    

class Water:
    def __init__(self, row, col):
        self.display = "W"
        self.row = row
        self.col = col

    def step():
        return '\n' +"Thank the Honourable Furious Forest, you've found a bucket of water!\n"
    
class Teleport:
    def __init__(self, display, row, col):
        self.display = display
        self.row = row
        self.col = col
    
    def step():
        return "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."   

