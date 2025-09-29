sample = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

direction_offset = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

direction_right = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

def get_guard_pos(grid):
    for i, row in enumerate(grid):
        if ('^' in row):
            return (i, row.index('^'))
        
def check_loop(grid, start_dir, start):
    pos = start
    direction = start_dir
    positions = set()

    while(True):
        nextPos = (pos[0] + direction_offset[direction][0], pos[1] + direction_offset[direction][1])
        if (not (nextPos[0] < len(grid) and nextPos[0] >= 0 and nextPos[1] < len(grid[0]) and nextPos[1] >= 0)):
            return False
        elif (grid[nextPos[0]][nextPos[1]] == '#'):
            direction = direction_right[direction]
            nextPos = (pos[0] + direction_offset[direction][0], pos[1] + direction_offset[direction][1])

        pos = nextPos
        foo = (nextPos[0], nextPos[1], direction)
        if (foo in positions):
            return True
        positions.add(foo)

def process_2(lines):
    count = 0
    grid = [list(l) for l in lines]
    pos = get_guard_pos(grid)
    direction = 'N'

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] != '.'): continue
            grid[i][j] = '#'
            if (check_loop(grid, direction, pos)):
                count += 1
            grid[i][j] = '.'
    print(count)

def process_1(lines):
    grid = [list(l) for l in lines]
    pos = get_guard_pos(grid)
    direction = 'N'
    positions = { pos }

    while(True):
        nextPos = (pos[0] + direction_offset[direction][0], pos[1] + direction_offset[direction][1])
        if (not (nextPos[0] < len(grid) and nextPos[0] >= 0 and nextPos[1] < len(grid[0]) and nextPos[1] >= 0)):
            break
        if (grid[nextPos[0]][nextPos[1]] == '#'):
            direction = direction_right[direction]
            nextPos = (pos[0] + direction_offset[direction][0], pos[1] + direction_offset[direction][1])
        pos = nextPos
        positions.add(pos)
    print(len(positions))

def main():
    with open('./inputs/2024/day6.txt') as f:
        lines = f.readlines()
        process_2([l.strip() for l in lines])
        #process_2(sample.split('\n')[1:-1])

if __name__ == '__main__':
    main()
