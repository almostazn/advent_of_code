day_11_input = '0 89741 316108 7641 756 9 7832357 91'
sample = '125 17'

num_blinks = 75

cache = {}

def blink_stones(stones):
    blinked_stones = []
    for stone in stones:
        if stone == 0:
            blinked_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            blinked_stones.append( int(stone_str[:len(stone_str)//2]) )
            blinked_stones.append( int(stone_str[len(stone_str)//2:]) )
        else:
            blinked_stones.append(stone * 2024)
    return blinked_stones

def blink_stones_recursive(stone, i):
    if (stone, i) in cache:
        return cache[(stone, i)]
    elif i == 0:
        return 1
    elif stone == 0:
        res = blink_stones_recursive(1, i - 1)
        cache[(1, i-1)] = res
        return res
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        res = blink_stones_recursive( int(stone_str[:len(stone_str)//2]), i - 1 )
        res_1 = blink_stones_recursive( int(stone_str[len(stone_str)//2:]), i -1 )

        cache[ (int(stone_str[:len(stone_str)//2]), i - 1) ] = res
        cache[  (int(stone_str[len(stone_str)//2:]), i - 1) ] = res_1
        return res + res_1
    else:
        res = blink_stones_recursive(stone * 2024, i - 1)
        cache[(stone * 2024, i -1)] = res
        return res

def process_2(line):
    stones = [int(n) for n in line.split()]
    print(stones)

    count = 0
    for stone in stones:
        #blinked_stones = [stone]
        #for i in range(num_blinks):
        count += blink_stones_recursive(stone, num_blinks)
    
    print(count)

def process_1(line):
    stones = [int(n) for n in line.split()]
    for i in range(num_blinks):
        stones = blink_stones(stones, i)
    print(len(stones))
    pass 


def main():
    process_2(day_11_input)
    #process_2(sample)

if __name__ == '__main__':
    main()
