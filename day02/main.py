def part1(name):

    with open(name) as file:
        result = 0
        lines = file.readlines()
        ranges = lines[0].split(',')
        for one_range in ranges:
            # print(one_range)
            start, finish = one_range.split('-')
            for i in range(int(start), int(finish)+1):
                # print(i)
                number = str(i)
                # print(number[:len(number)//2])
                # print(number[len(number)//2:])
                if (number[:len(number)//2] == number[len(number)//2:]):
                    result += i
    return result

def main():
    print("should be 1227775554")
    print(part1('day02/test.txt'))
    print(part1('day02/data.txt'))

if __name__ == "__main__":
    main()