
MAX_ADJACENT = 4

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0,-1)
DOWN = (0,1)
DIAGONAL_1 = (1,1)
DIAGONAL_2 = (-1,1)
DIAGONAL_3 = (1,-1)
DIAGONAL_4 = (-1,-1)

OFFSETS = [LEFT, RIGHT, UP, DOWN, DIAGONAL_1, DIAGONAL_2, DIAGONAL_3, DIAGONAL_4]

example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def is_inbound(coord, grid):
    x,y = coord
    return not (x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]))

def is_accessible(coord, grid):
    roll_count = 0

    for offset in OFFSETS:
        x,y = tuple(x + y for x, y in zip(coord, offset)) 

        if is_inbound((x, y), grid) and grid[y][x] == '@':
                roll_count += 1

    return roll_count < MAX_ADJACENT

def update_grid(grid, removed_rolls):
    for removed_roll in removed_rolls:
        x,y = removed_roll
        grid[y][x] = '.'

def main():
    with open('../inputs/2025/day4.txt') as f:
        grid = [ list(line.strip()) for line in f.readlines() ]
        # grid = [ list(line.strip()) for line in example.split() ]

        total_count = 0
        
        while True:
            removed_rolls = []
            count = 0

            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == '@' and is_accessible((x, y), grid):
                        removed_rolls.append((x, y))
                        count += 1

            if count == 0:
                break
            
            update_grid(grid, removed_rolls)
            total_count += count

        print(total_count)

if __name__ == '__main__':
    main()
