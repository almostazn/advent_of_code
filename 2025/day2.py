

import re

example="""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def is_invalid(sequence):
    if (len(sequence) % 2 == 1):
        return False

    midpoint = len(sequence) // 2

    return sequence[:midpoint] == sequence[midpoint:]

def is_repeating(s):
    return bool(re.fullmatch(r"(.+)\1+", s))

def main():
    with open('../inputs/2025/day2.txt') as f:
        for line in f.readlines():
            data = example
            ranges = data.split(',')

            count = 0
            for r in ranges:
                start, end = r.split('-')

                for i in range(int(start), int(end) + 1):
                    if (is_repeating(str(i))):
                        count += i

            print(count)

if __name__ == '__main__':
    main()
