example = """
987654321111111
811111111111119
234234234234278
898181911112111
"""

NUM_LENGTH = 12

def get_bank_jolt(bank):
    digits = [(char, idx) for idx, char in enumerate(bank) if char.isdigit()]
    first_digit = max(digits[:-1], key= lambda x: (x[0], -x[1]))

    second_digit = max(digits[first_digit[1]+1:])

    return int(f"{first_digit[0]}{second_digit[0]}")

def get_bank_jolt_2(bank):
    digits = [(char, idx) for idx, char in enumerate(bank) if char.isdigit()]
    digits.sort(key = lambda x: (x[0], -x[1]), reverse=True)

    best_digits = []
    current_bound = -1
    while len(best_digits) < NUM_LENGTH:
        lower_bound = len(digits) - (NUM_LENGTH - len(best_digits))

        for digit, idx in digits:
            if idx <= lower_bound and idx > current_bound:
                best_digits.append(digit)
                current_bound = idx
                break

    return int(''.join(best_digits))

def main():
    with open('../inputs/2025/day3.txt') as f:

        count = 0
        # for line in example.split():
        for line in f.readlines():
            bank = line.strip()
            count += get_bank_jolt_2(bank)

        print(count)

if __name__ == '__main__':
    main()

