from collections import defaultdict

sample = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

def in_bounds(grid, p):
    return p[0] >= 0 and p[1] >= 0 and p[1] < len(grid) and p[0] < len(grid[0])

def process_2(lines):
    grid = [list(l) for l in lines]
    antinodes = set()
    atennas = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                atennas[grid[i][j]].append((j,i))
    for points in atennas.values():
        for p1 in points:
            for p2 in points:
                if p1 == p2: continue
                current = p1
                while(True):
                    antinode1 = ( (p2[0] - p1[0]) + current[0], (p2[1] - p1[1]) + current[1] ) 
                    if in_bounds(grid, antinode1):
                        antinodes.add(antinode1)
                        current = antinode1
                    else: 
                        break
                
                current = p2
                while(True):
                    antinode2 = ( (p1[0] - p2[0]) + current[0],  (p1[1] - p2[1]) + current[1])
                    if in_bounds(grid, antinode2):
                        antinodes.add(antinode2)
                        current = antinode2
                    else: 
                        break

    print(len(antinodes))

def process_1(lines):
    grid = [list(l) for l in lines]
    antinodes = set()
    atennas = defaultdict(list)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '.':
                atennas[grid[i][j]].append((j,i))
    for points in atennas.values():
        for p1 in points:
            for p2 in points:
                if p1 == p2: continue
                antinode1 = ( 2* p1[0] - p2[0], 2* p1[1] - p2[1])
                antinode2 = ( 2* p2[0] - p1[0], 2* p2[1] - p1[1])
                if in_bounds(grid, antinode1): antinodes.add(antinode1)
                if in_bounds(grid, antinode2): antinodes.add(antinode2)
    print(len(antinodes))

def main():
    with open('./inputs/2024/day8.txt') as f:
        lines = [l.strip() for l in f.readlines()]
        process_2(lines)
        #process_2(sample.split('\n')[1:-1])


if __name__ == '__main__':
    main()
