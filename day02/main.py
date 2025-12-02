def check_pattern(number, pattern):
    pattern_len = len(pattern)
    if (len(number)/pattern_len != len(number)//pattern_len):
        return 0
    for i in range(1, len(number)//pattern_len):
        # print(number[pattern_len*i:pattern_len*(i+1)])
        if number[pattern_len*i:pattern_len*(i+1)] != pattern:
            return 0
    print(f'FOUND {number}')
    return 1

def part2(name):
    with open(name) as file:
        result = 0
        ranges = file.read().split(',')
        for one_range in ranges:
            # print(one_range)
            start, finish = one_range.split('-')
            for i in range(int(start), int(finish)+1):
                # print(f'number {i}')
                number = str(i)
                for j in range(1,len(number)//2+1):
                    # print(j)
                    pattern = number[:j]
                    # print(f'pattern {pattern}')
                    if (check_pattern(number, pattern)):
                        result += i
                        break
    return result

def part1(name):
    with open(name) as file:
        result = 0
        ranges = file.read().split(',')
        for one_range in ranges:
            # print(one_range)
            start, finish = one_range.split('-')
            for i in range(int(start), int(finish)+1):
                # print(i)
                number = str(i)
                if (number[:len(number)//2] == number[len(number)//2:]):
                    result += i
    return result


def main():
    print("1227775554 should be")
    print(part1('day02/test.txt'))
    print(part1('day02/data.txt'))

    # print("should be 4174379265")
    # print(part2('day02/test.txt'))
    # print(part2('day02/data.txt'))

if __name__ == "__main__":
    main()