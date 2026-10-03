import math

example = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

def main():
    with open('../inputs/2025/day6.txt') as f:
        rows = []
        operations = []


        # for line in example.strip().split('\n'):
        for line in f.readlines():
            if line[0] == '*' or line[0] == '+':
                operations = line.strip().split()
            else:
                # rows.append(list(line.replace(' ','#')))
                rows.append(list(line.strip().replace(' ','#')))

        matrix = []
        current = []
        for col in range(len(rows[0])):
            num = ''.join([rows[row][col] for row in range(len(rows))]).replace('#', '')
            if num == '':
                matrix.append(current)
                current = []
                continue
            current.append(int(num))
        matrix.append(current)

        count = 0
        for i in range(len(matrix)):
            nums = matrix[i]
            if operations[i] == '*':
                count += math.prod(nums)
            else:
                count += sum(nums)

        print(count)

if __name__ == '__main__':
    main()
