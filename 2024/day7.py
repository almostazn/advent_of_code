sample = '''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

def check_equation(current, nums):
    if (len(nums) == 1):
        return current == nums[0]
    return check_equation(current, [nums[0] + nums[1]] +  nums[2:]) or check_equation(current, [nums[0] * nums[1]] + nums[2:]) or check_equation(current, [ int(str(nums[0]) + str(nums[1])) ] +  nums[2:]) 

def process_1(lines):
    count = 0
    for line in lines:
        split_line = line.split(':')
        line_sum = int(split_line[0])
        nums = [int(n.strip()) for n in split_line[-1].split(' ') if n != '']
        if (check_equation(line_sum, nums)):
            count += line_sum

    print(count)

def main():
    with open('./inputs/2024/day7.txt') as f:
        lines = f.readlines()
        process_1([l.strip() for l in lines])
        #process_1(sample.split('\n')[1:-1])

if __name__ == '__main__':
    main()

