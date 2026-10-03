
MAX_NUM = 100
START = 50

example = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def main():
    with open('../inputs/2025/day1.txt') as f:
        rotationCount = 0
        current = START

        for line in f.readlines():
            rotation = line[0]
            num = int(line[1:])

            rotationCount += num // MAX_NUM
            num = num % MAX_NUM

            if (rotation == 'R'):
                newCurrent = current + num
            else:
                newCurrent = current - num

            if (current != 0 and (newCurrent <= 0 or newCurrent >= MAX_NUM)):
                rotationCount += 1

            current = newCurrent % MAX_NUM



        print(rotationCount)


if __name__ == '__main__':
    main()
