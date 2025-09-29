sample = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

offsets = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

def getTrailheads(grid):
    l = []
    for i, row in enumerate(grid):
        for j, e in enumerate(row):
            if grid[i][j] == 0:
                l.append( (i,j) )
    return l

def process_2(lines):
    grid = [ [ int(l) for l in list(line)] for line in lines]
    trailHeads = getTrailheads(grid)

    count = 0
    for trailHead in trailHeads:
        q = [trailHead]
        while len(q) != 0:
            current = q.pop()

            elevation = grid[current[0]][current[1]]

            if elevation == 9:
                count += 1
                continue

            for offset in offsets.values():
                newPos = (current[0] + offset[0], current[1] + offset[1])
                if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= len(grid) or newPos[1] >= len(grid[0]):
                    continue

                if grid[newPos[0]][newPos[1]] == elevation + 1:
                    q.append(newPos)
    print(count)


def process_1(lines):
    grid = [ [ int(l) for l in list(line)] for line in lines]
    trailHeads = getTrailheads(grid)

    count = 0
    for trailHead in trailHeads:
        seen = set()
        q = [trailHead]
        while len(q) != 0:
            current = q.pop()
            seen.add(current)

            elevation = grid[current[0]][current[1]]

            if elevation == 9:
                count += 1
                continue

            for offset in offsets.values():
                newPos = (current[0] + offset[0], current[1] + offset[1])
                if newPos[0] < 0 or newPos[1] < 0 or newPos[0] >= len(grid) or newPos[1] >= len(grid[0]):
                    continue

                if newPos not in seen and grid[newPos[0]][newPos[1]] == elevation + 1:
                    q.append(newPos)
    print(count)

def main():
    with open('./inputs/2024/day10.txt') as f:
        lines = [l.strip() for l in f.readlines()]
        process_2(lines)
        #process_2(sample.split('\n')[1:-1])

if __name__ == '__main__':
    main()
