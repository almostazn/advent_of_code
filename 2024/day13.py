import re

sample = '''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279'''

BUTTON_REGEX = r"Button (A|B): X\+(\d+), Y\+(\d+)"
PRIZE_REGEX = r"Prize: X=(\d+), Y=(\d+)"

PART_2 = 0
BUTTON_A_COST = 3

def parse_row(row):
    claw = {}
    a_match = re.match(BUTTON_REGEX, row[0])
    claw[a_match.group(1)] = ( int(a_match.group(2)), int(a_match.group(3)) )

    b_match = re.match(BUTTON_REGEX, row[1])
    claw[b_match.group(1)] = (int(b_match.group(2)), int(b_match.group(3)))

    p_match = re.match(PRIZE_REGEX, row[2])
    claw['P'] = (int(p_match.group(1)), int(p_match.group(2)))

    return claw

# Ax + Bx = Px
# Ay + By = Py
def get_pushes(a, b, c):
    a1, a2 = a
    b1, b2 = b
    c1, c2 = c
    c1 += PART_2
    c2 += PART_2
    x = ((c1 * b2) - (b1 * c2)) / ((a1 * b2) - (b1 * a2))
    y = ((a1 * c2) - (c1 * a2)) / ((a1 * b2) - (b1 * a2))

    return x, y

## no less than 180 presses
def process_1(lines):
    count = 0
    for line in lines:
      stuff = parse_row(line)
      cost = get_pushes(stuff['A'], stuff['B'], stuff['P'])
      if cost and int(cost[0]) == cost[0] and int(cost[1]) == cost[1]:
        count += (cost[0] * BUTTON_A_COST + cost[1])
    print(count)

def main():
    with open('./inputs/2024/day13.txt') as f:
        lines = []
        lines = f.read().split('\n\n')
        lines = [line.split('\n') for line in lines]
        process_1(lines)
        #sample_parse = [ s.split('\n') for s in sample.split('\n\n')]
        #process_1(sample_parse)


if __name__ == '__main__':
    main()
