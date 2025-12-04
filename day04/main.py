directions = [[-1,-1], [0,-1], [1,-1],
              [-1,0],          [1,0],
              [-1,1],  [0,1],  [1,1]]

def part2(name):
    with open(name) as file:
        grid = {}
        result = 0
        for y, line in enumerate(file.readlines()):
            for x, item in enumerate(line.strip()):
                if item == "@":
                    grid[(x,y)] = '@'
        while 1:
            can_be_removed = []
            for item in grid:
                counter = 0
                for dir in directions:
                    if (item[0]+dir[0], item[1]+dir[1]) in grid:
                        counter += 1
                if counter < 4:
                    can_be_removed.append(item)
            result += len(can_be_removed)
            if len(can_be_removed) == 0:
                return result
            for item in can_be_removed:
                grid.pop(item)
    return result


def part1(name):
    grid = {}
    with open(name) as file:
        result = 0
        for y, line in enumerate(file.readlines()):
            for x, item in enumerate(line.strip()):
                if item == "@":
                    grid[(x,y)] = '@'
        for item in grid:
            counter = 0
            for dir in directions:
                if (item[0]+dir[0], item[1]+dir[1]) in grid:
                    counter += 1
            if counter < 4:
                result += 1 

    return result


def main():
    print("13 should be")
    print(part1('day04/test.txt'))
    print(part1('day04/data.txt'))

    print("43 should be")
    print(part2('day04/test.txt'))
    print(part2('day04/data.txt'))

if __name__ == "__main__":
    main()