from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport, Player
)


def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    try:
        f = open(filename, 'r')
        file = f.readlines()
        return file
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        exit()




def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells (objects)
    """
    empty_list = [] #We will append the elements of lines to this list, thereby creating a list of lists
     
    valid_strings = [" ","*","\n", "X", "Y", "W", "F", '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    #Uses this list to check if file has unknown character
    teleportelement = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] #These are numbers that act as teleportation platforms
    test_teleportelement = [] #tests if teleport pads come exactly in pairs

    count_X = 0
    count_Y = 0
    count_teleport_number = 0
    i = 0
    while i<len(lines):
        empty_list.append(list(lines[i]))
        i += 1
    j=0
    while j < len(empty_list):
        a = 0
        while a < len(empty_list[j]):
            if empty_list[j][a] not in valid_strings:
                raise ValueError("Bad letter in configuration file: {}.".format(empty_list[j][a]))
            if empty_list[j][a] == "X":
                count_X += 1
            if empty_list[j][a] == "Y":
                count_Y += 1
            if empty_list[j][a] in teleportelement:
                test_teleportelement.append(empty_list[j][a])
                count_teleport_number += 1

            a+=1
        j+=1
    
    if count_X != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(count_X)) #Checks that there is exactly one 'X', else raises an error

    if count_Y != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(count_Y)) #Checks that there is exactly one 'Y', elses raises an error


    
    
    k = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0

    while k<len(test_teleportelement):
        if test_teleportelement[k] == '1':
            count_1 += 1
        elif test_teleportelement[k] == '2':
            count_2 += 1
        elif test_teleportelement[k] == '3':
            count_3 += 1
        elif test_teleportelement[k] == '4':
            count_4 += 1
        elif test_teleportelement[k] == '5':
            count_5 += 1
        elif test_teleportelement[k] == '6':
            count_6 += 1
        elif test_teleportelement[k] == '7':
            count_7 += 1
        elif test_teleportelement[k] == '8':
            count_8 += 1
        elif test_teleportelement[k] == '9':
            count_9 += 1
        k  += 1

        #if count_1 !=2 or count2 != 2 or count3 != 2 ... or count9 != 2:
        #number = 

        #raise ValueError("Teleport pad {} does not have an exclusively matching pad".format[number])

        if count_1!=2 and count_teleport_number %2 != 0:
            raise ValueError("Teleport pad 1 does not have an exclusively matching pad.")
        elif count_2!=2 and count_teleport_number %2 !=0 :
            raise ValueError("Teleport pad 2 does not have an exclusively matching pad.")
        elif count_3!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 3 does not have an exclusively matching pad.")
        elif count_4!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 4 does not have an exclusively matching pad.")
        elif count_5!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 5 does not have an exclusively matching pad.")
        elif count_6!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 6 does not have an exclusively matching pad.")
        elif count_7!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 7 does not have an exclusively matching pad.")
        elif count_8!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 8 does not have an exclusively matching pad.")
        elif count_9!=2 and count_teleport_number % 2 !=0:
            raise ValueError("Teleport pad 9 does not have an exclusively matching pad.")


        # this ultimately tests that there are exactly ONE pair of teleport numbers,

    list_of_list_objects = []
    i = 0
    row = 0
    while i<len(lines):
        a = 0
        cell_line = []
        col = 0
        while a<len(lines[i]):
            cell = lines[i][a]
            if cell == "F":
                cell_line.append(Fire(row, col))
            elif cell == "W":
                cell_line.append(Water(row, col))
            elif cell == " ":
                cell_line.append(Air(row, col))
            elif cell == "*":
                cell_line.append(Wall(row, col))
            elif cell == "X":
                cell_line.append(Player(0, row, col))
            elif cell == "Y":
                cell_line.append(End(row, col))
            elif cell in teleportelement:
                cell_line.append(Teleport(cell, row, col))
            col += 1
            a += 1
        row += 1
        i += 1
        list_of_list_objects.append(cell_line)
        

    return list_of_list_objects


def find_player(ls):
    for x in ls:
        for a in x:
            if a.display == "A":
                return a
