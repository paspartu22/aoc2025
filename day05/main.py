def part1(name):
    with open(name) as file:
        result = 0
        ranges_lines, inputs = file.read().split('\n\n')
        ranges = []
        for line in ranges_lines.split('\n'):
            ranges.append(line.split('-'))
        # print(ranges)
        # print (inputs)
        for input in inputs.split('\n'):
            for range in ranges:
                if int(input) <= int(range[1]) and int(input) >= int(range[0]):
                    result += 1
                    break
    return result


def part2(name):
    with open(name) as file:
        result = 0
        ranges = {}
        range_num = 0
        for i,line in enumerate(file.read().split('\n\n')[0].split('\n')):
            line = line.split('-')
            ranges[i] = [int(line[0]),int(line[1])]
            range_num = i+1

        while(1):
            changes_done = 0
            for x in range(range_num):
                for y in range(range_num):
                    if x != y and x in ranges and y in ranges:
                        if ranges[x][0] <= ranges[y][0] and ranges[x][1] >= ranges[y][0]:
                            if  ranges[x][1] <= ranges[y][1]:
                                ranges[x][1] = ranges[y][1]
                            del ranges[y]
                            changes_done = 1

            if changes_done == 0:
                for i, complete_range in enumerate(ranges.values()):
                    # print (f'{i} \t {complete_range} \t {complete_range[1] - complete_range[0] + 1}')
                    result += complete_range[1] - complete_range[0] + 1
                return result      
    return result

def main():
    print("3 should be")
    print(part1('day05/test.txt'))
    print(part1('day05/data.txt'))

    print("14 should be")
    print(part2('day05/test.txt'))
    print(part2('day05/data.txt'))

if __name__ == "__main__":
    main()