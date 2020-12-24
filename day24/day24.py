target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def find_tile(instructions):
    instructions = list(instructions)
    x = 0
    y = 0
    change_line = 0
    for direction in instructions:
        if direction == 'e':
            if change_line == 1:
                y += 1
                x += 1
                change_line = 0
            elif change_line == -1:
                y -= 1
                x += 1
                change_line = 0
            else:
                x += 2
        elif direction == 'n':
            change_line = 1
        elif direction == 's':
            change_line = -1
        else:
            if change_line == 1:
                y += 1
                x -= 1
                change_line = 0
            elif change_line == -1:
                y -= 1
                x -= 1
                change_line = 0
            else:
                x -= 2
    return(x, y)

def paint(painted, tile):
    if tile not in painted:
        painted[tile] = "black"
    else:
        painted[tile] = "white"

painted = {}
for instructions in data:
    tile = find_tile(instructions)
    paint(painted, tile)

total = 0
for value in painted.values():
    if value == "black":
        total += 1

print(total)