from collections import defaultdict

def draw(splitters, beam, max_x, max_y):
    for y in range(max_y):
        line = ""
        for x in range(max_x):
            if (x, y) in splitters:
                line += '^'
            elif y in beam and x in beam[y]:
                line += '|'
            else:
                line += '.'
        print(line)

def part1(name):
    with open(name) as file:
        splitters = []
        beam = {0:set()}
        result = 0
        max_y, max_x = 0,0

        for y, line in enumerate(file.readlines()):
            max_y = y+1
            for x, item in enumerate(line.strip()):
                max_x = x+1
                if item == '^':
                    splitters.append((x,y))
                if item == 'S':
                    beam[y].add(x)
        draw(splitters, beam, max_x, max_y)
        print()
        for y in range(max_y):
            beam[y+1] = set()
            for x in range(max_x):
                if x in beam[y]:
                    if (x, y+1) not in splitters:
                        beam[y+1].add(x)
                    else:
                        result+=1   
                        beam[y+1].add(x-1)
                        beam[y+1].add(x+1)
        draw(splitters, beam, max_x, max_y)
    return result


def part2(name):
    with open(name) as file:
        splitters = []
        beam = {0:defaultdict(int)}
        max_y, max_x = 0,0

        for y, line in enumerate(file.readlines()):
            max_y = y+1
            for x, item in enumerate(line.strip()):
                max_x = x+1
                if item == '^':
                    splitters.append((x,y))
                if item == 'S':
                    beam[y][x] = 1
        draw(splitters, beam, max_x, max_y)
        print()
        for y in range(max_y):
            beam[y+1] = defaultdict(int)
            for x in range(max_x):   
                if x in beam[y]:             
                    if (x, y+1) not in splitters:
                        beam[y+1][x] += beam[y][x]

                    else:
                        beam[y+1][x-1] += beam[y][x]
                        beam[y+1][x+1] += beam[y][x]
        draw(splitters, beam, max_x, max_y)
    return sum(beam[max_y].values())




def main():
    print(" should be")
    # print(part1('day07/test.txt'))
    # print(part1('day07/data.txt'))

    # print(" should be")
    print(part2('day07/test.txt'))
    print(part2('day07/data.txt'))

if __name__ == "__main__":
    main()